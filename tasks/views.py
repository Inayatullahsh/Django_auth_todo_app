from django.shortcuts import render, redirect
from datetime import datetime

from .models import Task
from .forms import TaskModelForm
# Create your views here.


def index(request):
    weekday = {
        '1': "Sunday 🖖",
        '2': "Monday 💪😀",
        '3': "Tuesday 😜",
        '4': "Wednesday 😌☕️",
        '5': "Thursday 🤗",
        '6': "Friday 🍻",
        '7': "Saturday 😴"
    }

    form = TaskModelForm()
    task_list = Task.objects.order_by('id')

    today = datetime.now().strftime('%w')
    context = {
        'form': form,
        'task_list': task_list,
        'today': weekday[today]
    }
    return render(request, 'tasks/index.html', context)


def addTask(request):
    form = TaskModelForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect('index')


def completeTask(request, task_id):
    item = Task.objects.get(pk=task_id)

    if item.complete:
        item.complete = False
        item.save()
    else:
        item.complete = True
        item.save()

    return redirect('index')


def deleteTask(request, task_id):
    item = Task.objects.get(pk=task_id)

    item.delete()

    return redirect('index')
