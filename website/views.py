from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.gzip import gzip_page
from django.contrib import messages
from django.utils import timezone
from general import models
from events.models import Event

from django.conf import settings

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from django.db import IntegrityError


@gzip_page
def home(request):
    '''Site homepage for CompSoc'''
    template = 'home.html'

    upcoming_event = Event.objects.all().filter(ongoing_event=False).order_by('start_time').first

    context = {
        "event": upcoming_event
    }

    return render(request, template, context)


@gzip_page
def members(request):
    '''Members page'''
    context = {}
    context['current'] = models.CompMember.objects.filter(alumni=False).order_by('name')
    context['alumni'] = models.CompMember.objects.filter(alumni=True).order_by('-batch_of', 'name')
    return render(request, 'members.html', context)


@gzip_page
def signup(request):
    '''Signup view'''
    template = 'auth/signup.html'
    context = {}

    if request.method == 'POST' and not request.user.is_authenticated():
        firstname = request.POST['firstname'].title()
        lastname = request.POST['lastname'].title()
        username = request.POST['username']
        email = request.POST['email'].lower()
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # create_user
            try:
                user = User.objects.create_user(first_name=firstname,
                                                last_name=lastname,
                                                username=username,
                                                email=email,
                                                password=password)
                user.save()
            except IntegrityError:
                messages.error(request, 'Sorry! The username is already taken. Try again!')
                return redirect(signup)
            messages.info(request, 'Now, please login!')
            return redirect(login)
        else:
            messages.error(request, "Sorry, your passwords didn't match. Try again!")
            return redirect(signup)
    elif request.user.is_authenticated():
        messages.info(request, "You're already logged in!")
        return redirect(home)
    else:
        return render(request, template, context)


# Auth Views
@gzip_page
def login(request):
    '''Login view'''
    template = 'auth/login.html'
    context = {}

    if request.method == 'POST' and not request.user.is_authenticated():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, 'You have logged in successfully!')
                if 'events.orfik' in settings.INSTALLED_APPS:
                    messages.info(request, 'Read the instructions and then play!')
                    return redirect(reverse('events:orfik:home'))
                return redirect(home)
            else:
                messages.error(request, 'Something went wrong. Try again!')
                return redirect(login)
        else:
            messages.error(request, 'You entered the wrong username or password. Try again!')
            return redirect(login)
    elif request.user.is_authenticated():
        messages.info(request, "You're already logged in!")
        if 'events.orfik' in settings.INSTALLED_APPS:
            messages.info(request, 'Read the instructions and then play!')
            return redirect(reverse('events:orfik:home'))
        return redirect(home)
    else:
        return render(request, template, context)


@gzip_page
def logout(request):
    '''Logout view'''
    auth_logout(request)
    messages.info(request, "Logged out!")
    return redirect(home)


def time(request):
    '''Time'''
    template = 'time.html'
    context = {}
    now = timezone.now()
    context['hour'] = bin(now.hour)
    context['minute'] = bin(now.minute)
    context['second'] = bin(now.second)
    return render(request, template, context)
