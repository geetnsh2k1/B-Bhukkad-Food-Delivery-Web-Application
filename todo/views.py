from django.shortcuts import render, redirect
from todo.models import Task
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

# Create your views here.
def addtask(request):
    if request.method == "POST":
        try:
            username = request.user.username
            user = User.objects.get(username=username)

            task = request.POST['task']

            newtask = Task.objects.create(user=user, task=task, time=str(datetime.datetime.now()), status=False)
            newtask.save()
            messages.success(request, 'new task added to the list.')
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('profile')

def deletetask(request):
    if request.method == "POST":
        try:
            username = request.user.username
            user = User.objects.get(username=username)
            task = request.POST['task']

            dtask = Task.objects.get(user=user, task__iexact=task)
            dtask.delete()
        except Exception as e:
            print(e)
    else:
        pass
    return redirect('profile')