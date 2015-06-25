from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as NewUser
from django.views.decorators.gzip import gzip_page
from general import models


@gzip_page
def home(request):
    '''Site homepage for CompSoc'''
    template = 'home.html'
    return render(request, template)


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
def register(request):
    '''Register a user account'''
    data = {}
    template = 'auth/register.html'
    if request.method == 'GET':
        data['register_form'] = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            data['register_form'] = form
    return render(request, template, data)
