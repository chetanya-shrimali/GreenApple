from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from drop_a_note.forms import NoteForm
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from validate_email import validate_email
from django.contrib import messages


def drop_note(request):
    return render(request, 'drop_a_note/contact.html')


@csrf_protect
def contact_us(request):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            notes = note_form.save(commit=False)
            email_address = note_form.cleaned_data['email']
            note_content = note_form.cleaned_data['note']
            name = note_form.cleaned_data['name']
            print(email_address + " -> " + str(name) + " -> " + str(
                note_content))
            notes.save()

            value = validate_email(email_address, verify=True)
            print(value)
            if value is None:
                return HttpResponse("invalid mail")
            else:
                email = EmailMessage('Regarding feedback',
                                     email_address + "\n\n" + note_content,
                                     to=['chetanyashrimalie5@gmail.com',
                                         'nkchoudhary696@gmail.com'])
                email.send()

                email = EmailMessage('Regarding feedback',
                                     "Hey " + name + ",\n\n" + "We have "
                                                               "successfully"
                                                               " recieved "
                                                               "your note!!",
                                     to=[email_address])
                email.send()
                print('reached')
                return HttpResponseRedirect(reverse('home:index'))
        else:
            print(note_form.errors)
            return redirect('home/index.html')

    else:
        note_form = NoteForm()

    return render(request, 'drop_a_note/contact.html',
                  {'note_form': note_form})
