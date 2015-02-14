from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm as NewUser
from website import models
def home(request):
    """Site homepage for compsoc
    """
    data={}
    template='base.html'
    return render(request,template,data)
def contact(request):
    """Contact page"""
    return render(request,'contact.html')
def about(request):
    "About us"
    data={}
    data['current']=models.CompMember.objects.filter(alumni=False)
    data['alumni']=models.CompMember.objects.filter(alumni=True)
    return render(request,'about.html',data)
def register(request):
    "Register a user account"
    data={}
    template='register.html'
    if request.method=='GET':
        data['register_form']=NewUser()
    if request.method=='POST':
        form=NewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:data['register_form']=form
    return render(request,template,data)
