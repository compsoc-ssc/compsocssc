from django.shortcuts import render,redirect,get_object_or_404
from orfik import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from general import models as generalmodels
def home(request):
    data={}
    template='orfik/home.html'
    if request.user.is_authenticated():
        try:
            player=request.user.player
        except:
            user=request.user
            p=models.Player()
            p.nickname=user.username
            p.user=request.user
            p.save()
            data['new_nick_form']=models.NickForm()
        #get the questions available
        data['questions']=models.Question.objects.filter(number__lte=request.user.player.max_level).order_by('number')
        if request.method=='POST':
            form=models.Nickform(request.POST)
            if form.is_valid():form.save()
    data['starttime']=generalmodels.Variable.objects.get(name='orfikstart')
    return render(request,template,data)
def instructions(request):
    return render(request,'orfik/instructions.html')
def leader(request):
    data={}
    template='orfik/leader.html'
    data['players']=models.Player.objects.all().order_by('-max_level','-last_solve')
    return render(request,template,data)

#------------------private things
@login_required
def hint(request,q_no):
    q_no=int(q_no)
    #if player has not reached question
    if player.max_level<q_no:return redirect('orfik:hint',q_no=player.max_level)
    #-------------------
    data={}
    template='orfik/hint.html'
    player=request.user.player
    question=get_object_or_404(models.Question,number=q_no)
    data['hints']=models.Aid.objects.filter(question=question)
    data['question']=question
    return render(request,template,data)
@login_required
def question(request,q_no):
    starttime=generalmodels.Variable.objects.get('orfikstart').time
    #Check if orfik has started
    if starttime>timezone.now():return redirect('orfik:home')
    q_no=int(q_no)
    #if player has not reached question
    if player.max_level<q_no:return redirect('orfik:question',q_no=player.max_level)
    #----------------------
    data={}
    template='orfik/question.html'
    player=request.user.player
    question=get_object_or_404(models.Question,number=q_no)
    if request.method=='GET':
        data['form']=models.AnswerForm()
        data['question']=question
    if request.method=='POST':
        form=models.AnswerForm(request.POST)
        if question.number==player.max_level:#This is his first potential
            #correct answer
            if form.is_valid():
                attempt=form.save(commit=False)
                attempt.player=player
                attempt.question=question
                attempt.save()
                if attempt.is_correct():
                    player.last_solve=timezone.now()
                    player.max_level+=1
                    player.save()
                    return redirect('orfik:question',q_no=question.number+1)
            else:
                data['form']=form
                data['question']=question
        return render(request,template,data)
