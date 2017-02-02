from django.shortcuts import render, redirect
from events.logo.models import Submission
from events.logo.forms import SubmissionForm
from general import models as generalmodels
from django.utils import timezone
from events import models as event_models


def check_end(event):
    return event.end_time <= timezone.now()


def home(request):
    template = 'logo/home.html'
    return render(request, template)


def gallery(request):
    data = {}
    template = 'logo/gallery.html'
    data['pics'] = Submission.objects.all().values('logo', 'name')
    return render(request, template, data)


def submission(request):
    data = {}
    template = 'logo/submission.html'
    logo = event_models.Event.objects.filter(appname='logo').order_by('start_time').last()
    data['ended'] = check_end(logo)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:logo:success')
        else:
            print(form.is_valid())
    else:
        form = SubmissionForm()
    data['form'] = form
    return render(request, template, data)


def success(request):
    template = 'logo/success.html'
    return render(request, template)
