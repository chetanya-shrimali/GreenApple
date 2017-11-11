from django.shortcuts import render


def drop_note(request):
    return render(request, 'drop_a_note/contact.html')
