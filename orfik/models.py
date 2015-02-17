from django import forms
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Player(models.Model):
    def __str__(self):return self.nickname
    nickname=models.CharField(max_length=20)
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    max_level=models.SmallIntegerField(default=0)
    last_solve=models.DateTimeField(default=timezone.now())

class Question(models.Model):
    def __str__(self):return str(self.number)+':'+self.text[:15]+' ...'
    number=models.SmallIntegerField()
    text=models.TextField()
    image=models.ImageField(upload_to='question',blank=True,null=True)
    answer=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('question',kwargs={'q_no':self.number})
class Aid(models.Model):
    question=models.ForeignKey(Question,related_name='aid')
    text=models.TextField(blank=True)
    image=models.ImageField(upload_to='question/aid',blank=True,null=True)
class Attempt(models.Model):
    player=models.ForeignKey(Player,related_name='player_attempt')
    question=models.ForeignKey(Question,related_name='attempt')
    value=models.CharField(max_length=100)
    correct=models.NullBooleanField(default=None)
    def is_correct(self):
        if self.correct!=None:return self.correct
        if self.question.answer==self.value:self.correct=True
        else:self.correct=False
        return self.correct
#------------forms
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Attempt
        exclude=['player','question','correct']
class NickForm(forms.ModelForm):
    class Meta:
        model=Player
        fields=['nickname']
