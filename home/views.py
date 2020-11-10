from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json
from home.models import Customer

# Create your views here.
def home(request):
    try:
        if request.user.is_authenticated:
            username = request.user.username
            user = User.objects.get(username=username)

            customer = Customer.objects.get(user=user)

            count = 0

            if customer.phone == None or customer.phone == "":
                count+=1
            else:
                pass
            if customer.address == None or customer.address == "":
                count += 1
            else:
                pass

            return render(request, 'home.html', {'count':count})
        else:
            pass
    except Exception as e:
        print(e, 'error')
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

def viewprofile(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
        customer = Customer.objects.get(user=user) 
        count = 0
        if customer.phone == None or customer.phone == "":
            count += 1
        if customer.address == None or customer.address == "":
            count += 1
        return render(request, 'profile.html', {'customer':customer, 'count':count})
    except Exception as e:
        print(e)
        messages.error(request, 'error while loading your profile')
        return redirect('home')

def account(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
        customer = Customer.objects.get(user=user) 
        return render(request, 'account.html', {'customer':customer})
    except Exception as e:
        print(e)
        messages.error(request, 'error while loading your profile')
        return redirect('home')
    
def addadress(request):
    if request.method == "POST":
        address = request.POST['address']
        username = request.user.username
        user = User.objects.get(username=username)
        customer = Customer.objects.get(user=user)
        customer.address = address
        customer.save()
        print('hi, it;s working')
    else:
        pass
    return redirect('account')

def updateaddress(request):
    if request.method == "POST":
        try:
            newaddress = request.POST['newaddress']
            username = request.user.username
            user = User.objects.get(username=username)
            customer = Customer.objects.get(user=user)
            customer.address = newaddress
            customer.save()
        except:
            pass
    else:
        pass
    return redirect('account')