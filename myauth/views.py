from django.shortcuts import render


def login(request):
    template = 'myauth/login.html'
    context = {
        'request': request,
        'user': request.user
    }
    return render(request, template, context)

