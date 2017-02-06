from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Max


from events import models as event_models
from events.orfik import models, utils



def make_player(request):
    try:
        player = request.user.player
    except:
        user = request.user
        p = models.Player()
        p.nickname = user.username
        p.user = request.user
        p.save()


def check_end(event):
    return event.end_time <= timezone.now()


def check_start(event):
    return event.start_time <= timezone.now()


def home(request):
    data = {}
    template = 'orfik/home.html'
    orfik = event_models.Event.objects.filter(appname='orfik').order_by('start_time').last()
    data['starttime'] = orfik.start_time
    data['started'] = check_start(orfik)
    if request.user.is_authenticated():
        make_player(request)
        data['new_nick_form'] = models.NickForm()
        ended = check_end(orfik)
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
    orfik = event_models.Event.objects.filter(appname='orfik').order_by('start_time').last()
    max_question = models.Question.objects.filter(event=orfik).aggregate(Max('number'))
    max_question = max_question['number__max']
    data['players'] = models.Player.objects.all().order_by('-max_level','last_solve')
    if orfik.end_time <= timezone.now():
        data['winner'] = data['players'][0]
    attempts = models.Attempt.objects.filter(question__event=orfik, correct=True).order_by('stamp')
    data['image'] = utils.get_plot_string(attempts, orfik, max_question)
    return render(request, template, data)


@login_required
def question(request, q_no):
    make_player(request)
    orfik = event_models.Event.objects.filter(appname='orfik').order_by('start_time').last()
    starttime = orfik.start_time
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
        if check_end(orfik):
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
