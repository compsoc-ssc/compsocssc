from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as NewUser
from django.views.decorators.gzip import gzip_page
# from django.contrib import messages
from django.views.decorators.gzip import gzip_page
from general import models
from events.models import Event


@gzip_page
def home(request):
    '''Site homepage for CompSoc'''
    template = 'home.html'

    upcoming_event = Event.objects.all().order_by('start_time').first

    context = {
        "event": upcoming_event
    }

    return render(request, template, context)


@gzip_page
def contact(request):
    '''Contact page'''
    return render(request, 'contact.html')


@gzip_page
def members(request):
    '''Members page'''
    data = {}
    data['current'] = models.CompMember.objects.filter(alumni=False)
    data['alumni'] = models.CompMember.objects.filter(alumni=True)
    return render(request, 'members.html', data)

# Auth Views
@gzip_page
def login(request):
    '''Login view'''
    template = 'auth/login.html'


    return render(request, template, context)


@gzip_page
def signup(request):
    '''Signup view'''
    template = 'auth/signup.html'
    context = {}



    return render(request, template, context)


@gzip_page
def password_reset(request):
    '''Password reset view'''
    template = 'auth/password_reset.html'
    context = {}



    return render(request, template, context)
