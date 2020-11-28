from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from home.models import Customer
from food_items.models import Cart

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created == True:
        c = Customer.objects.create(user=instance)
        Cart.objects.create(customer=c)
        print('Customer Created')

@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):
    if created == False:
        instance.customer.save()
        print('Customer Updated')