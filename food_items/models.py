from django.db import models
from django.contrib.auth.models import User
import datetime
from home.models import Customer

# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    status = models.BooleanField(default=True)
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default_restaurant.png', blank=True)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, null=False)
    email = models.EmailField(default="nomail@gamil.com")
    number = models.IntegerField()
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    location = models.TextField()
    services = models.CharField(max_length=100, default="BREAKFAST LUNCH DINNER CAFE NIGHTLIGHT")
    alcohol = models.BooleanField(default=False)
    cuisines = models.CharField(max_length=200, default="")
    confirm = models.BooleanField(default=False)
    opened = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(blank=False)
    cuisine = models.CharField(max_length=100, blank=True, null=True)
    diet = models.CharField(max_length=10, default="veg")
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class ItemPerQuantity(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    itemtotal = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.item.name)+str('-')+str(self.quantity)

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    itemperquantity = models.ManyToManyField(ItemPerQuantity, related_name='itemperquantity', null=True, blank=True)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.customer.user.username)+str('-')+str(self.total)

class Delivery(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliveryaddress = models.CharField(max_length=100)
    typeofaddress = models.CharField(max_length=10, default="HOME")

    def __str__(self):
        return self.customer.user.username

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cust')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default="")
    deliveryaddress = models.CharField(max_length=150)
    item = models.CharField(max_length=200, null=True)
    total = models.FloatField()
    placed = models.DateTimeField(auto_now_add=True)
    deliverytime = models.CharField(max_length=100, blank=True)
    status = models.TextField(default="Your order has been placed.")
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.customer) + str('-') + str(self.approved)

class Pending(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rest')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
    item = models.ForeignKey(ItemPerQuantity, on_delete=models.CASCADE, related_name='items', null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.restaurant.name) + str('-') + str(self.customer) + str('-') + str(self.status)
    
class History(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="")
    item = models.CharField(max_length=150, default="")
    placed = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.restaurant.name) + str('-') + str(self.item)
    
class Earning(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    earning = models.FloatField(default=0.0)
    
    def __str__(self):    
        return str(self.restaurant.name) + str('-') + str(self.earning)
