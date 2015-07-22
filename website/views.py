from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as NewUser
from django.views.decorators.gzip import gzip_page
from general import models
from events.models import Event


def home(request):
    '''Site homepage for CompSoc'''
    template = 'home.html'

    upcoming_event = Event.objects.all().order_by('start_time').first

    context = {
        "event": upcoming_event
    }

    return render(request, template, context)


def contact(request):
    '''Contact page'''
    return render(request, 'contact.html')


def members(request):
    '''Members page'''
    data = {}
    data['current'] = models.CompMember.objects.filter(alumni=False)
    data['alumni'] = models.CompMember.objects.filter(alumni=True)
    return render(request, 'members.html', data)

# Auth Views
def login(request):
    '''Login view'''
    template = 'auth/login.html'
    context = {}



    return render(request, template, context)


def signup(request):
    '''Signup view'''
    template = 'auth/signup.html'
    context = {}



    return render(request, template, context)


def password_reset(request):
    '''Password reset view'''
    template = 'auth/password_reset.html'
    context = {}



    return render(request, template, context)
