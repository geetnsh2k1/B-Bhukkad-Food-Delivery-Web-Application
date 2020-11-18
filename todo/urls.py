from django.urls import path, include, re_path
from django.conf.urls import url
from todo import views

urlpatterns = [
    path('addtask/', views.addtask),
    path('deletetask/', views.deletetask),
]