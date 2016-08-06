from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

from .forms import NewMemberForm
from django.contrib import messages


def new_member_form(request):
    form = NewMemberForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('success')
        else:
            messages.error(request, "There were errors with the form. Fix and try again!")
    context = { 'form': form, }
    return render(request, 'join/join_form.html', context)


def join_success(request):
    return render(request, 'join/join_success.html')
