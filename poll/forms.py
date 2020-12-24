from django import forms
from django.contrib.auth.models import User
from .models import *


class QuestionForm(forms.ModelForm):
    title = forms.CharField(label='',
        widget=forms.TextInput(attrs = { "placeholder": "Your salary", "class": "form-control" }))
    # start_date = forms.CharField(label='',
    #     widget=forms.TextInput(attrs = { "placeholder": "Your salary", "class": "form-control" }))
    status = forms.CharField(label='Salary',
        widget=forms.TextInput(attrs = { "placeholder": "Your salary", "class": "form-control" }))

    class Meta:
        model = Question
        fields = [
            'title',
            'status',
            'start_date',
            'end_date'
        ]
