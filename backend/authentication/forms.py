from asyncio import tasks
from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import logo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class logoform(forms.ModelForm):
    class Meta:
        model=logo
        fields=['logo_name','item']


class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=101)
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    student_id=forms.CharField(max_length=101)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['student_id','username','first_name', 'last_name', 'email', 'password1', 'password2']
