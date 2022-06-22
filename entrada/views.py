from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from entrada.forms import RegisterForm
import email
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')
