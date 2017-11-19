from book_a_table.forms import BookForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
# from django.apps import apps
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from validate_email import validate_email


@csrf_protect
def book_table(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            table = book_form.save()
            customer = book_form.cleaned_data['customer']
            contact = book_form.cleaned_data['contact']
            email_send = book_form.cleaned_data['email']
            total_persons = book_form.cleaned_data['total_persons']
            date = book_form.cleaned_data['date']
            time = book_form.cleaned_data['time']
            table.save()

            value = validate_email(email_send, verify=True)
            print(value)
            if value is None:
                return HttpResponse("invalid mail")
            else:
                email = EmailMessage('Regarding Booking a Table',
                                     "Recieved mail from " + str(
                                         email_send) + "\n\n" + "name: " +
                                     str(customer) + "\n" + "contact: " +
                                     str(contact) + "\npersons: " +
                                     str(total_persons) + "\n" +
                                     "date and time: " + str(
                                         date) + "  " + str(time),
                                     to=['chetanyashrimalie5@gmail.com', ])
                email.send()

                email = EmailMessage('Regarding Booking a Table',
                                     "Hey " + str(
                                         customer) + ",\n\n" + "We have "
                                                               "recieved "
                                                               "your request "
                                                               "for book a "
                                                               "table\n" +
                                     "We will contact you shortly on " +
                                     str(contact),
                                     to=[email_send,
                                         'chetanyashrimalie5@gmail.com'],
                                     reply_to=[email_send, ])
                email.send()
                print('reached')
                return HttpResponseRedirect(reverse('home:index'))
        else:
            print(book_form.errors)
            return redirect('home/index.html')
    else:
        book_form = BookForm()

    return render(request, 'book_a_table/reservations.html',
                  {'book_form': book_form})
