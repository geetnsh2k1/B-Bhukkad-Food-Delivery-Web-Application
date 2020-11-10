from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=11, decimal_places=0, null=True, blank=True)
    address = models.TextField(blank=True, null=True)                             
    picture = models.ImageField(default='default.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username