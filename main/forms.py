from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = crudUser
        fields = ['firstname', 'lastname', 'email', 'password']

class deleteForm(forms.ModelForm):
    class Meta:
        model = deleteModel
        fields = '__all__'
