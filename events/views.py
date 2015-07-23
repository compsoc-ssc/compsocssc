from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

from events.models import Event


@gzip_page
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
