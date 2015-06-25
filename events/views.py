from django.shortcuts import redirect
from django.shortcuts import render


def home(request):
    '''
    View for the Events home page
    '''
    template = 'events/home.html'
    return render(request, template)

