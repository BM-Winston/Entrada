from dataclasses import fields
import email
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *




class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'url']
        exclude = ['user']