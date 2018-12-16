from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signup(request):
    if request.method == "POST":
        new_user = User.objects.create_user(username = request.POST['name'], password = request.POST['password'])
        login(request, new_user)
        return redirect('/posts')
    else:
        return render(request, 'member/signup.html')

def signin(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/posts')
        else:
            return render(request, 'member/signin.html', {'status':1})
    else:
        return render(request, 'member/signin.html', {'status':0})

def check(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/signin')