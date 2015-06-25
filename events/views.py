from django.shortcuts import redirect
from django.shortcuts import render


def home(request):
    '''
    View for the Events home page
    '''
    template = 'events/home.html'
    return render(request, template)


# def register(request):
#     '''Register a user account'''
#     data = {}
#     template = 'auth/register.html'
#     if request.method == 'GET':
#         data['register_form'] = NewUser()
#     if request.method == 'POST':
#         form = NewUser(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             data['register_form'] = form
#     return render(request, template, data)

