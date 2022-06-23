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

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('login')

@login_required(login_url='/accounts/login/')
def posts(request):

    post = Post.objects.all()
    return render(request,'posts.html',{'post':post})

