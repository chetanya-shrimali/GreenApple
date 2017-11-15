from book_a_table.forms import BookForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# from django.apps import apps
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from validate_email import validate_email
from django.contrib import messages

# def book(request):
#     return render(request, 'book_a_table/reservations.html')


# class BookFormView(View):
#     form_class = BookForm
#     template_name = 'book_a_table/reservations.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, 'book_a_table/reservations.html',
#                       {'form': form})
#
#     def post(self):
#         pass
#
#
# class CustomerFormView(View):
#     form_class = apps.get_model('order.Customer')
#     template_name = 'book_a_table/customer_registration.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request,
#                       'book_a_table/../order/templates/order/customer_registration.html',
#                       {'form': form})
#
#     def post(self):
#         pass


@csrf_protect
def book_table(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            table = book_form.save()
            customer = book_form.cleaned_data['customer']
            # contact = book_form.cleaned_data['contact']
            email = book_form.cleaned_data['email']
            # total_persons = book_form.cleaned_data['total_persons']
            # date = book_form.cleaned_data['date']
            # time = book_form.cleaned_data['time']
            table.save()
            
            value = validate_email(email, verify=True)
            print(value)
            if value is None:
                messages.error(request, 'enter valid email',)
                # return HttpResponse("invalid mail")
            else:
                email = EmailMessage('Regarding Booking a Table',
                                     email + "\n\n" + customer,
                                     to=['chetanyashrimalie5@gmail.com',
                                         'nkchoudhary696@gmail.com'])
                email.send()

                email = EmailMessage('Regarding Booking a Table',
                                     "Hey " + customer + ",\n\n" + "We have successfully Booked your Table!!",
                                     to=[email])
                email.send()
                print('reached')
                return HttpResponseRedirect(reverse('home:index'))
        else:
            print(book_form.errors)
            return redirect('home/index.html')
    else:
        book_form = BookForm()

    return render(request, 'book_a_table/reservations.html', {'book_form': book_form})
