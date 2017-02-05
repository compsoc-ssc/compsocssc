from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from django import forms
from events import models as event_models


class Player(models.Model):
    def __str__(self):
        return self.nickname
    nickname = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    max_level = models.SmallIntegerField(default=0)
    last_solve = models.DateTimeField(default=timezone.now)


class Question(models.Model):
    number = models.SmallIntegerField()
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='question', blank=True, null=True)
    answer = models.CharField(max_length=100)
    event = models.ForeignKey(event_models.Event, related_name='event_question')

    def __str__(self):
        return str(self.number) + ':' + self.text[:15] + ' ...'

    def get_absolute_url(self):
        return reverse('orfik:question', kwargs={'q_no': self.number})


class Attempt(models.Model):
    player = models.ForeignKey(Player, related_name='player_attempt')
    question = models.ForeignKey(Question, related_name='attempt')
    value = models.CharField(max_length=100)
    correct = models.NullBooleanField(default=None)
    stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def is_correct(self):
        if self.correct is None:
            self.correct = self.question.answer.lower() == self.value.lower()
            self.save()
        return self.correct


class AnswerForm(forms.ModelForm):
    value = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Answer'}), label='')
    class Meta:
        model = Attempt
        exclude = ['player', 'question', 'correct']


class NickForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nickname']
