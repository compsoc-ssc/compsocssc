from django.shortcuts import render, redirect
from .models import Submission
from .forms import SubmissionForm


def home(request):
    template = 'logo/home.html'
    return render(request, template)


def submission(request):
    data = {}
    template = 'logo/submission.html'
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
