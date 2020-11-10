from django.urls import path, include, re_path
from django.conf.urls import url
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.handlelogin),
    re_path(r'[a-zA-Z0-9/!@#$%^&*]*logout[a-zA-Z0-9/!@#$%^&*]*', views.handlelogout),
    path('signup/', views.handlesignup),
    path('viewprofile/', views.viewprofile),
    path('viewprofile/account/', views.account, name='account'),
    path('viewprofile/account/addaddress/', views.addadress),
    path('viewprofile/account/updateaddress/', views.updateaddress),
]