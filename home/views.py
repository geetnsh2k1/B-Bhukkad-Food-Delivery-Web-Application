from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json
from home.models import Customer

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handlelogin(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'you have successfully logged in')
            else:
                user = User.objects.filter(username=username)
                if len(user) != 0:
                    messages.error(request, 'Incorrect Password')
                else:
                    string = 'no account with this username, ' + str(username) +  ' ~> go sign up'
                    messages.error(request, string)
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('home')

def handlelogout(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
    return redirect('home')

def handlesignup(request):
    if request.method == "POST":
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirm = request.POST['confirm']
            
            user = User.objects.filter(username=username)

            if len(user) == 0:
                if password == confirm:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                    user.save()
                    messages.success(request, 'account successfully created')
                else:
                    messages.error(request, 'password confirmation failed')
            else:
                messages.error(request, 'user already exists')

        except Exception as e:
            print(e)
    else:
        pass
    return redirect('home')