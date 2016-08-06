from django import forms
from .models import NewMember

class NewMemberForm(forms.ModelForm):
    class Meta:
        model = NewMember
        exclude = ['timestamp']
        labels = {
            'name': "FULL NAME",
            'course': "COURSE",
            'year': "YEAR",
            'phone_number': "PHONE NUMBER",
            'email': "EMAIL",
        }

