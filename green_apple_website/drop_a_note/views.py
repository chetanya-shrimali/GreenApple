from django.contrib import messages
from django.contrib.messages import constants as messages
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from drop_a_note.forms import *
from validate_email import validate_email

MESSAGE_TAGS = {
    messages.ERROR: '',
    50: 'critical',
}


def drop_note(request):
    return render(request, 'drop_a_note/contact.html')


def my(request):
    messages.add_message(request, messages.ERROR, 'Enter Valid Message!!')

    return render(request, 'drop_a_note/contact.html', {})


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
            # notes.save()

            value = validate_email(email_address, verify=True)
            print(value)
            if value is None:
                messages.add_message(request, messages.ERROR, 'Enter Valid Message!!')
                # return HttpResponse("invalid mail")
            else:
                email = EmailMessage('Regarding feedback',
                                     email_address + "\n\n" + note_content,
                                     to=['chetanyashrimalie5@gmail.com',
                                         'nkchoudhary696@gmail.com'])
                email.send()

                email = EmailMessage('Regarding feedback',
                                     "Hey " + name + ",\n\n" + "We have successfully received your note!!",
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
