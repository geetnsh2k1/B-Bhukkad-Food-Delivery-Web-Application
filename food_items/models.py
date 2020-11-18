from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(blank=False)

    def __str__(self):
        return self.name

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
    items = models.ManyToManyField(Item, related_name='items', null=True, blank=True)
    services = models.CharField(max_length=100, default="BREAKFAST LUNCH DINNER CAFE NIGHTLIGHT")
    alcohol = models.BooleanField(default=False)
    cuisines = models.CharField(max_length=200, default="")
    confirm = models.BooleanField(default=False)
    opened = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name