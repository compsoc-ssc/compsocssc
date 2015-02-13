from django.shortcuts import render,redirect

def home(request):
    """Site homepage for compsoc
    """
    data={}
    template='base.html'
    return render(request,template,data)
def contact(request):
    """Contact page"""
    data={}
    template='contact.html'
    return render(request,template,data)
