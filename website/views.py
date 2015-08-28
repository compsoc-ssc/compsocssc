from django.shortcuts import render, redirect
from django.views.decorators.gzip import gzip_page
from django.contrib import messages
from general import models
from events.models import Event

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from django.db import IntegrityError


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
                # Message: Username is taken
                return redirect(signup)
            # Message: please login
            return redirect(login)
        else:
            # failure message
            return redirect(signup)
    elif request.user.is_authenticated():
        # Message: you're already logged in
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
                print ("yay")
                auth_login(request, user)
                return redirect(home)
            else:
                # Show failure message
                print ("fail")
                return redirect(login)
        else:
            # Show wrong credentials message
            print ("wrong")
            return redirect(login)
    elif request.user.is_authenticated():
        # Message: you're already logged in
        return redirect(home)
    else:
        return render(request, template, context)


@gzip_page
def logout(request):
    '''Logout view'''
    auth_logout(request)
    # Success message
    return redirect(home)


# Later
@gzip_page
def password_reset(request):
    '''Password reset view'''
    template = 'auth/password_reset.html'
    context = {}

    return render(request, template, context)
