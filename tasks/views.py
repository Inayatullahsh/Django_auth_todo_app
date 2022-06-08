from django.urls import reverse
from django.db.transaction import commit
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskModelForm
# Create your views here.


def homepage(request):
    weekday = {
        '0': "Sunday 🖖",
        '1': "Monday 💪😀",
        '2': "Tuesday 😜",
        '3': "Wednesday 😌☕️",
        '4': "Thursday 🤗",
        '5': "Friday 🍻",
        '6': "Saturday 😴"
    }

    form = TaskModelForm()

    try:
        task_list = Task.objects.filter(user=request.user.pk)
    except Task.DoesNotExist:
        task_list = None
    today = datetime.now().strftime('%w')
    context = {
        'form': form,
        'task_list': task_list,
        'today': weekday[today]
    }
    return render(request, 'index.html', context)


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
