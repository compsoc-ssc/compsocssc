from django.shortcuts import render, redirect
from django.views.decorators.gzip import gzip_page
from django.contrib import messages
from general import models
from events.models import Event

from django.conf import settings

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from django.contrib import messages

from django.db import IntegrityError

from django.core.mail import send_mail


@gzip_page
def home(request):
    '''Site homepage for CompSoc'''
    template = 'home.html'

    upcoming_event = Event.objects.all().order_by('start_time').first

    context = {
        "event": upcoming_event
    }

    if request.method == 'POST':
        # Someone wants to write to CompSoc
        name = request.POST['name'].title()
        from_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST.get('message')

        to_email = [settings.EMAIL_HOST_USER,]

        send_mail(subject, message, from_email, to_email, fail_silently=True)

        messages.info(request, "Your email has been sent. We will get back to you shortly!")
        return redirect(home)

    return render(request, template, context)


@gzip_page
def members(request):
    '''Members page'''
    context = {}
    context['current'] = models.CompMember.objects.filter(alumni=False)
    context['alumni'] = models.CompMember.objects.filter(alumni=True)
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
            # Passwords don't match. Handle with JS
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
                return redirect(home)
            else:
                messages.error(request, 'Something went wrong. Try again!')
                return redirect(login)
        else:
            messages.error(request, 'You entered the wrong username or password. Try again!')
            return redirect(login)
    elif request.user.is_authenticated():
        messages.info(request, "You're already logged in!")
        return redirect(home)
    else:
        return render(request, template, context)


@gzip_page
def logout(request):
    '''Logout view'''
    auth_logout(request)
    messages.info(request, "Logged out!")
    return redirect(home)


# Later
@gzip_page
def password_reset(request):
    '''Password reset view'''
    template = 'auth/password_reset.html'
    context = {}

    return render(request, template, context)
