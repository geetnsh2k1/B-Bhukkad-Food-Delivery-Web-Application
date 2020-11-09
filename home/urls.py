from django.urls import path, include, re_path
from django.conf.urls import url
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.handlelogin),
    path('logout/', views.handlelogout),
    path('signup/', views.handlesignup),
]