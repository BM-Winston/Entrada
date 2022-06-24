from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from entrada.forms import PostForm, RegisterForm
import email
from django.contrib import messages
from .models import Profile, Post

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

@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('posts')
    else:
        form = PostForm()
    return render(request,'add_post.html',{'form':form})

@login_required(login_url='/accounts/login/')
def search_posts(request):
    if 'flask' in request.GET and request.GET['flask']:
        searchTerm = request.GET.get('flask')
        postResults = Post.get_post(searchTerm)     
        return render(request,'search.html',{'results':postResults})

    else:
        message = 'You have not searched for any term'
        return render(request,'search.html',{'message':message})
