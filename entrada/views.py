from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from entrada.forms import RegisterForm
import email
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()   

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

