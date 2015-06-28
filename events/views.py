from django.shortcuts import redirect
from django.shortcuts import render

from events.models import Event


def home(request):
    '''
    View for the Events home page
    '''
    template = 'events/home.html'
    events = Event.objects.all().order_by('start_time')

    context = {
        "events": events
    }
    
    return render(request, template, context)
