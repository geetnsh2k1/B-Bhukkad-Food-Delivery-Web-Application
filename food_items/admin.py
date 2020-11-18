from django.contrib import admin
from food_items.models import Restaurant, Item, Owner

# Register your models here.
admin.site.register(Item)
admin.site.register(Restaurant)
admin.site.register(Owner)