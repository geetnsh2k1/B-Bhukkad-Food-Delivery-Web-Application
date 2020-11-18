from django.urls import path, include, re_path
from django.conf.urls import url
from food_items import views

urlpatterns = [
    path('addrestaurant/', views.addrestaurant),
    path('addrestaurant/formsubmission/', views.addrestaurantform),
]
