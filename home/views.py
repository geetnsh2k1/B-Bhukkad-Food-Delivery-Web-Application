from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json
from home.models import Customer
from django.http import JsonResponse
from food_items.models import Restaurant, Item, Owner, Location
import os
from Food_Delievery.settings import MEDIA_ROOT
from todo.models import Task
import datetime

# Create your views here.
def home(request):
    try:
        if request.user.is_authenticated:
            username = request.user.username
            user = User.objects.get(username=username)

            customer = Customer.objects.get(user=user)

            count = 0

            location_json = json.dumps(list(Location.objects.values()))
            restaurants = Restaurant.objects.all()

            if customer.phone == None or customer.phone == "":
                count+=1
            else:
                pass
            if customer.address == None or customer.address == "":
                count += 1
            else:
                pass

            return render(request, 'home.html', {'count':count, 'restaurants':restaurants, 'location_json':location_json})
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
        
        if request.user.is_superuser:
            newrestaurants = Restaurant.objects.filter(confirm=False).all()
            newrestaurants_count = Restaurant.objects.filter(confirm=False).all().count()
            working_restaurants = Restaurant.objects.filter(confirm=True).count()
            customers_count = Customer.objects.all().count()
            owners_count = Owner.objects.all().count()
            customers = Customer.objects.all()
            restaurants = Restaurant.objects.filter(confirm=True)
            owners = Owner.objects.all()

            # CUSTOMERS
            january_customers = Customer.objects.filter(created__icontains='-01-').count()
            feb_customers = Customer.objects.filter(created__icontains='-02-').count()
            march_customers = Customer.objects.filter(created__icontains='-03-').count()
            april_customers = Customer.objects.filter(created__icontains='-04-').count()
            may_customers = Customer.objects.filter(created__icontains='-05-').count()
            june_customers = Customer.objects.filter(created__icontains='-06-').count()
            july_customers = Customer.objects.filter(created__icontains='-07-').count()
            august_customers = Customer.objects.filter(created__icontains='-08-').count()
            september_customers = Customer.objects.filter(created__icontains='-09-').count()
            october_customers = Customer.objects.filter(created__icontains='-10-').count()
            november_customers = Customer.objects.filter(created__icontains='-11-').count()
            december_customers = Customer.objects.filter(created__icontains='-12-').count()

            # RESTAURANTS
            january_restaurants = Restaurant.objects.filter(opened__icontains='-01-', confirm=True).count()
            feb_restaurants = Restaurant.objects.filter(opened__icontains='-02-', confirm=True).count()
            march_restaurants = Restaurant.objects.filter(opened__icontains='-03-', confirm=True).count()
            april_restaurants = Restaurant.objects.filter(opened__icontains='-04-', confirm=True).count()
            may_restaurants = Restaurant.objects.filter(opened__icontains='-05-', confirm=True).count()
            june_restaurants = Restaurant.objects.filter(opened__icontains='-06-', confirm=True).count()
            july_restaurants = Restaurant.objects.filter(opened__icontains='-07-', confirm=True).count()
            august_restaurants = Restaurant.objects.filter(opened__icontains='-08-', confirm=True).count()
            september_restaurants = Restaurant.objects.filter(opened__icontains='-09-', confirm=True).count()
            october_restaurants = Restaurant.objects.filter(opened__icontains='-10-', confirm=True).count()
            november_restaurants = Restaurant.objects.filter(opened__icontains='-11-', confirm=True).count()
            december_restaurants = Restaurant.objects.filter(opened__icontains='-12-', confirm=True).count()

            # NEWREQUESTS
            january_requests = Restaurant.objects.filter(opened__icontains='-01-', confirm=False).count()
            feb_requests = Restaurant.objects.filter(opened__icontains='-02-', confirm=False).count()
            march_requests = Restaurant.objects.filter(opened__icontains='-03-', confirm=False).count()
            april_requests = Restaurant.objects.filter(opened__icontains='-04-', confirm=False).count()
            may_requests = Restaurant.objects.filter(opened__icontains='-05-', confirm=False).count()
            june_requests = Restaurant.objects.filter(opened__icontains='-06-', confirm=False).count()
            july_requests = Restaurant.objects.filter(opened__icontains='-07-', confirm=False).count()
            august_requests = Restaurant.objects.filter(opened__icontains='-08-', confirm=False).count()
            september_requests = Restaurant.objects.filter(opened__icontains='-09-', confirm=False).count()
            october_requests = Restaurant.objects.filter(opened__icontains='-10-', confirm=False).count()
            november_requests = Restaurant.objects.filter(opened__icontains='-11-', confirm=False).count()
            december_requests = Restaurant.objects.filter(opened__icontains='-12-', confirm=False).count()  

            # TASKS          
            tasks = Task.objects.filter(user=user)

            return render(request, 'profile.html', {'customer':customer, 'count':count, 'newrestaurants':newrestaurants, 'newrestaurants_count':newrestaurants_count,
            'working_restaurants':working_restaurants, 'customers_count':customers_count,
            'owners_count':owners_count, 'customers':customers, 'owners':owners, 'restaurants':restaurants, 'january_customers':january_customers, 'feb_customers':feb_customers, 'march_customers':march_customers, 'april_customers':april_customers, 'may_customers':may_customers, 'june_customers':june_customers, 'july_customers':july_customers, 'august_customers':august_customers, 'september_customers':september_customers, 'october_customers':october_customers, 'november_customers':november_customers,'december_customers':december_customers,'january_restaurants':january_restaurants, 'feb_restaurants':feb_restaurants, 'march_restaurants':march_restaurants, 'april_restaurants':april_restaurants, 'may_restaurants':may_restaurants, 'june_restaurants':june_restaurants, 'july_restaurants':july_restaurants, 'august_restaurants':august_restaurants, 'september_restaurants':september_restaurants, 'october_restaurants':october_restaurants,'november_restaurants':november_restaurants,'december_restaurants':december_restaurants, 'january_requests':january_requests, 'feb_requests':feb_requests,'march_requests':march_requests, 'april_requests':april_requests, 'may_requests':may_requests, 'june_requests':june_requests, 'july_requests':july_requests, 'august_requests':august_requests, 'september_requests':september_requests, 'october_requests':october_requests,'november_requests':november_requests, 'december_requests':december_requests, 'tasks':tasks})
        else:
            try:
                owner = Owner.objects.get(user=user)
                try:
                    restaurant = Restaurant.objects.get(owner=owner)
                    items = Item.objects.filter(restaurant=restaurant)
                    status = False
                    try:
                        print(restaurant.opened, type(restaurant.opened))
                        today = datetime.date.today()
                        if today == restaurant.opened:
                            status = True
                    except Exception as e:
                        print(e)
                    return render(request, 'profile.html', {'status':status, 'customer':customer, 'count':count, 'owner':owner,'restaurant':restaurant, 'items':items})                
                except Exception as e:
                    print(e)
                    # owner.delete()
                    return render(request, 'profile.html', {'customer':customer, 'count':count, 'owner':owner})                
            except:
                pass
        return render(request, 'profile.html', {'customer':customer, 'count':count})
    except Exception as e:
        print(e)
        messages.error(request, 'error while loading your profile')
        return redirect('home')

def get_customers_count_json(request):
    context = {
        'customers_count_json':Customer.objects.count()
    }
    return JsonResponse(context)

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

def addphone(request):
    if request.method == "POST":
        phone = request.POST['phone']
        username = request.user.username
        user = User.objects.get(username=username)
        customer = Customer.objects.get(user=user)
        customer.phone = phone
        customer.save()
    else:
        pass
    return redirect('account')

def updatephone(request):
    if request.method == "POST":
        try:
            newphone = request.POST['newphone']
            username = request.user.username
            user = User.objects.get(username=username)
            customer = Customer.objects.get(user=user)
            customer.phone = newphone
            customer.save()
        except:
            pass
    else:
        pass
    return redirect('account')

def editimage(request):
    if request.method == "POST":
        try:
            picture = request.FILES['image']
            username = request.user.username
            user = User.objects.get(username=username)
            customer = Customer.objects.get(user=user)

            initial_path = customer.picture.path
            
            initial_path = str(initial_path).split('\\')
            initial_path = initial_path[0:len(initial_path)-1]
            i_path = ''
            for i in initial_path:
                i_path += i
                i_path += str('\\')
            print(i_path)

            customer.picture = picture

            customer.save()
        except Exception as e:
            print(e, 'error')
    else:
        pass
    return redirect('account')

def viewprofile2(request):
    return redirect('profile')

# make it for working of specific location and find it;s restaurants
def handlelocation(request, location):
    print(location)
    restaurants = Restaurant.objects.filter(city=location)
    return render(request, 'location.html', {'location':location, 'restaurants':restaurants})

def handlelocationrestaurant(request, location, restaurant):
    try:
        rest = Restaurant.objects.get(name=restaurant)
        items = Item.objects.filter(restaurant=rest)
        return render(request, 'locationrestaurant.html', {'restaurant':rest, 'items':items})
    except Exception as e:
        print(e, 'error')
        messages.error(request, 'An unexcepted error occured while loading the restaurant.')
        return redirect('home')

def acceptrestaurant(request):
    if request.method == "POST":
        name = request.POST['name']
        restaurant = Restaurant.objects.get(name=name)
        restaurant.confirm = True
        restaurant.save()
        message = restaurant.name + ' is successfully added'
        messages.success(request, message)
        return redirect('profile')
    else:
        pass
    return redirect('home')

def rejectrestaurant(request):
    if request.method == "POST":
        name = request.POST['name']
        restaurant = Restaurant.objects.get(name=name)
        restaurant.delete()
        messages.error(request, 'Rejected')
        return redirect('profile')
    else:
        pass
    return redirect('home')

def removerestaurant(request):
    if request.method == "POST":
        try:
            restaurantname = request.POST['restaurantname']
            restaurant = Restaurant.objects.get(name=restaurantname)
            restaurant.owner.delete()
            restaurant.delete()
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('profile')

def removecustomer(request):
    if request.method == "POST":
        try:
            username = request.POST['customername']
            user = User.objects.get(username=username)
            customer = Customer.objects.get(user=user)
            customer.delete()
            try:
                owner = Owner.objects.get(user=user)
                restaurant = Restaurant.objects.get(owner=owner)
                owner.delete()
                restaurant.delete()
            except:
                pass
        except:
            pass
    else:
        pass
    return redirect('profile')

def additem(request):
    if request.method == "POST":
        try:
            username = request.user.username
            user = User.objects.get(username=username)
            owner = Owner.objects.get(user=user)
            restaurant = Restaurant.objects.get(owner=owner)

            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']
            cuisine = request.POST['cuisine']
            image = request.FILES['image']

            newitem = Item.objects.create(name=name, description=description, price=price, cuisine=cuisine, image=image)

            newitem.restaurant.add(restaurant)

            newitem.save()

            messages.success(request, 'item successfully added.')
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('profile')

def new_restaurants_request_json(request):
    restaurants = list(Restaurant.objects.filter(confirm=False).values())
    return JsonResponse({'restaurants':restaurants})

def owners_json(request):
    owners = list(Owner.objects.values())
    return JsonResponse({'owners':owners})

def users_json(request):
    users = list(User.objects.values())
    return JsonResponse({'users':users})