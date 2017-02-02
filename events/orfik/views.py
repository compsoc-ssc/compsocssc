from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest,HttpResponseRedirect
from events.orfik import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from general import models as generalmodels
from .models import CredentialsModel
from django.contrib import messages
from oauth2client import client
from apiclient import discovery
from django.core.urlresolvers import reverse
import httplib2
from website.settings.base import GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,SECRET_KEY
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from oauth2client.contrib import xsrfutil


FLOW = client.flow_from_clientsecrets(
    GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
    scope = 'https://www.googleapis.com/auth/calendar',
    redirect_uri='http://compsocssc.pythonanywhere.com/events/orfik/auth'
)


def make_player(request):
    try:
        player = request.user.player
    except:
        user = request.user
        p = models.Player()
        p.nickname = user.username
        p.user = request.user
        p.save()


def check_end():
    return generalmodels.Variable.objects.get(name='orfikend').time <= timezone.now()


def check_start():
    return generalmodels.Variable.objects.get(name='orfikstart').time <= timezone.now()


def home(request):
    data = {}
    template = 'orfik/home.html'
    data['starttime'] = generalmodels.Variable.objects.get(name='orfikstart').time
    data['started'] = check_start()
    if request.user.is_authenticated():
        make_player(request)
        data['new_nick_form'] = models.NickForm()
        ended = check_end()
        # Has orfik ended?
        if ended:
            data['endtime'] = ended
            data['winner'] = models.Player.objects.all().order_by('-max_level','last_solve')[0] == request.user.player
            return render(request, template, data)
        # If it has not ended, has it started?
        if data['started']:
            return redirect('events:orfik:question', q_no=0)
        # It has not started, get the available questions
        data['questions'] = models.Question.objects.filter(number__lte=request.user.player.max_level).order_by('number')
        if request.method == 'POST':
            form = models.Nickform(request.POST)
            if form.is_valid():
                form.save()
    return render(request, template, data)


def instructions(request):
    return render(request, 'orfik/instructions.html')


def leader(request):
    data = {}
    template = 'orfik/leader.html'
    endtime = generalmodels.Variable.objects.get(name='orfikend').time
    data['players'] = models.Player.objects.all().order_by('-max_level','last_solve')
    if endtime <= timezone.now():
        data['winner'] = data['players'][0]
    return render(request, template, data)


@login_required
def question(request, q_no):
    make_player(request)
    starttime = generalmodels.Variable.objects.get(name='orfikstart').time
    player = request.user.player
    # Check if orfik has started
    if starttime > timezone.now():
        return redirect('events:orfik:home')
    q_no = int(q_no)
    # If player is not on question
    if player.max_level != q_no:
        return redirect('events:orfik:question', q_no=player.max_level)

    data = {}
    template = 'orfik/question.html'
    question = get_object_or_404(models.Question,number=q_no)
    data['question'] = question
    if request.method == 'GET':
        data['form'] = models.AnswerForm()
    if request.method == 'POST':
        if check_end():
            return redirect('events:orfik:home')
        form = models.AnswerForm(request.POST)
        if question.number == player.max_level:  # This is his first potential
            # Correct answer
            if form.is_valid():
                attempt = form.save(commit=False)
                attempt.player = player
                attempt.question = question
                attempt.save()
                if attempt.is_correct():
                    player.last_solve = timezone.now()
                    player.max_level += 1
                    player.save()
                    messages.info(request, 'Corrent answer!')
                    return redirect('events:orfik:question', q_no=question.number+1)
                else:
                    messages.info(request, 'Wrong answer. Try again!')
                    return redirect('events:orfik:question', q_no=question.number)
            else:
                data['form'] = form
    return render(request, template, data)



@login_required()
def authorize(request):
    store = DjangoORMStorage(CredentialsModel,'id',request.user,'credential')
    credential = store.locked_get()
    if credential is None or credential.invalid == True:
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        calendar_service = discovery.build('calendar', 'v3', http=http)
        event = {
            'summary': 'Orfik 2017',
            'description': 'Orfik is Compsoc\'s online tech hunt.',
            'start': {
                'date': '2017-02-10',
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'date': '2017-02-11',
                'timeZone': 'Asia/Kolkata',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = calendar_service.events().insert(calendarId='primary', body=event).execute()

        messages.info(request, "Added to Calendar")
        return redirect(reverse('events:orfik:home'))

@login_required()
def add_event(request):
    credential = FLOW.step2_exchange(request.GET['code'])
    storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
    storage.put(credentials=credential)
    return authorize(request)