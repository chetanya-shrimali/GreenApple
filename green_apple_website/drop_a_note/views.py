from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from drop_a_note.forms import *
from django.views.decorators.csrf import csrf_protect


def drop_note(request):
    return render(request, 'drop_a_note/contact.html')


@csrf_protect
def contact_us(request):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            notes = note_form.save()
            notes.save()
            return HttpResponseRedirect(reverse('home:index'))
        else:
            print(note_form.errors)
            return redirect('home/index.html')

    else:
        note_form = NoteForm()

    return render(request, 'drop_a_note/contact.html', {'note_form': note_form})
