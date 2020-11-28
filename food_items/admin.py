from django.contrib import admin
from food_items.models import Restaurant, Item, Owner, Location, ItemPerQuantity, Cart, Delivery, Order, Pending, History, Earning

# Register your models here.
admin.site.register(Item)
admin.site.register(Restaurant)
admin.site.register(Owner)
admin.site.register(Location)
admin.site.register(ItemPerQuantity)
admin.site.register(Cart)
admin.site.register(Delivery)
admin.site.register(Order)
admin.site.register(Pending)
admin.site.register(History)
admin.site.register(Earning)