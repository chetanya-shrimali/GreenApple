from django.shortcuts import render
from drop_a_note.forms import *


def drop_note(request):
    return render(request, 'drop_a_note/contact.html')


def contact_us(request):
    if request.method == 'POST':
        contact_form = NoteForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            contact.save()
            return render(request, 'home/index.html', {})
        else:
            print(contact_form.errors)
            return redirect('home/index.html')

    else:
        contact_form = ContactForm()

    return render(request, 'home/contact.html', {'contact_form': contact_form})