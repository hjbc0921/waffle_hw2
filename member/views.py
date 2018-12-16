from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/posts')
    else:
        form = UserForm()
        return render(request, 'member/signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/posts')
        else:
            return render(request, 'member/signin.html', {'form': form, 'status':1})
    else:
        form = LoginForm()
        return render(request, 'member/signin.html', {'form': form, 'status':0})

def check(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/signin')