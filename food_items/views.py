from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from food_items.models import Item, Restaurant, Owner, Location
from django.contrib.auth.models import User
import json

# Create your views here.
def addrestaurant(request):
    try:
        user = request.user.username
        if user == "" or user == None:
            messages.error(request, 'you need to be logged in, to use it')
            return redirect('home')
        else:
            return render(request, 'addrestaurant.html')
    except Exception as e:
        error = e + str(' error')
        messages.error(request, error)
        return redirect('home')
    
def addrestaurantform(request):
    if request.method == "POST":
        try:
            username = request.user.username
            user = User.objects.get(username=username)

            ownername = request.POST['ownername']
            restaurantname = request.POST['restaurantname'] 
            ownernumber = request.POST['ownernumber']
            try:
                status = request.POST['status']
                if status == "This place is already open.":
                    status = True
                else:
                    status = False
            except:
                status = "This place is already open."
                status = True
            city = request.POST['city']
            city = city.upper()
            state = request.POST['state']
            state = state.upper()
            location = request.POST['location']
            location = location.upper()
            alcohol = request.POST['alcohol']
            if alcohol == "Doesn't Serves Alcohol":
                alcohol = False
            else:
                alcohol = True
            services = ""
            try:
                breakfast = request.POST['breakfast']
                services += str("BREAKFAST ")
            except:
                breakfast = "off"
    
            try:
                lunch = request.POST['lunch']
                services += str("LUNCH ")
            except:
                lunch = "off"
            
            try:
                dinner = request.POST['dinner']
                services += str("DINNER ")
            except:
                dinner = "off"
            
            try:
                cafe = request.POST['cafe']
                services += str("CAFE ")
            except:
                cafe = "off"
            
            try:
                nightlife = request.POST['nightlife']
                services += str("NIGHTLIFE ")
            except:
                nightlife = "off"
            try:
                cuisines = request.POST['cuisines']
            except:
                cuisines = ""
            email = request.POST['email']
            restaurantnumber = request.POST['phone']
            image = request.FILES['image']

            newowner = Owner.objects.create(user=user, restaurant_name=restaurantname, phone=ownernumber, status=status)
            newowner.save()

            newrestaurant = Restaurant.objects.create(name=restaurantname, image=image, owner=newowner, email=email, number=restaurantnumber, city=city, state=state, location=location, services=services, alcohol=alcohol, cuisines=cuisines)
            newrestaurant.save()

            newlocation = Location.objects.create(city=city, state=state)
            newlocation.save()

            messages.success(request, 'thank you, you will be updated soon.')

        except Exception as e:
            messages.error(request, 'sorry, try again an unexcepted error occured.')
            print(e,'error')
    else:
        pass
    return redirect('home')