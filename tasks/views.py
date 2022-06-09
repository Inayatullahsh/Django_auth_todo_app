from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import TaskModelForm
from .models import Task

# Create your views here.


@login_required
def addTask(request):
    form = TaskModelForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
    return redirect('homepage')


@login_required
def completeTask(request, task_id):
    item = Task.objects.get(pk=task_id)

    if item.is_completed:
        item.is_completed = False
        item.save()
    else:
        item.is_completed = True
        item.save()

    return redirect('homepage')


@login_required
def deleteTask(request, task_id):
    item = Task.objects.get(pk=task_id)

    item.delete()

    return redirect('homepage')
