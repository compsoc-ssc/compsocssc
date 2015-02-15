from django import forms
from logo.models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('name', 'college_name', 'email', 'phone', 'logo', 'tagline')
