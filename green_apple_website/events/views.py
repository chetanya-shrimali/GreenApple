from django.shortcuts import render

from .models import Event


def events(request):
    all_events = Event.objects.all()
    return render(request, 'events/events.html', {'all_events': all_events})
