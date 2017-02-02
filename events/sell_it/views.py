from django.shortcuts import render, redirect
from events.sell_it.models import Submission
from events.sell_it.forms import SubmissionForm
from general import models as generalmodels
from django.utils import timezone
from events import models as event_models


def check_end(event):
    return event.end_time <= timezone.now()


def home(request):
    template = 'sell_it/home.html'
    return render(request, template)


# def gallery(request):
#     data = {}
#     template = 'sell_it/gallery.html'
#     data['pics'] = Submission.objects.all().values('design', 'name')
#     return render(request, template, data)


def submission(request):
    data = {}
    template = 'sell_it/submission.html'
    sell_it = event_models.Event.objects.filter(appname='sell_it').order_by('start_time').last()
    data['ended'] = check_end(sell_it)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:sell_it:success')
        else:
            print(form.is_valid())
    else:
        form = SubmissionForm()
    data['form'] = form
    return render(request, template, data)


def success(request):
    template = 'sell_it/success.html'
    return render(request, template)
