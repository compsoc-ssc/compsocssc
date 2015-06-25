from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as NewUser
from django.views.decorators.gzip import gzip_page
from general import models


def home(request):
    '''Site homepage for CompSoc'''
    template = 'home.html'
    return render(request, template)


def contact(request):
    '''Contact page'''
    return render(request, 'contact.html')


def members(request):
    '''Members page'''
    data = {}
    data['current'] = models.CompMember.objects.filter(alumni=False)
    data['alumni'] = models.CompMember.objects.filter(alumni=True)
    return render(request, 'members.html', data)
