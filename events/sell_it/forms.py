from django import forms
from events.sell_it.models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('name', 'college_name', 'email', 'phone', 'design')
