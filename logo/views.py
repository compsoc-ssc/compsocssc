from django.shortcuts import render, redirect
from .models import Submission
from .forms import SubmissionForm
from general import models as generalmodels
from django.utils import timezone

def check_end():
    return generalmodels.Vriable.objects.get(name='logoend')<=timezone.now()
def home(request):
    template = 'logo/home.html'
    return render(request, template)
def gallery(request):
    data={}
    template='logo/gallery.html'
    data['pics']=Submission.objects.all().values('logo','name')
    print(data['pics'])
    return render(request,template,data)
def submission(request):
    data = {}
    template = 'logo/submission.html'
    data['ended']=check_end()
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logo:success')
        else:
            print(form.is_valid())
    else:
        form = SubmissionForm()
    data['form'] = form
    return render(request, template, data)


def success(request):
    template = 'logo/success.html'
    return render(request, template)
