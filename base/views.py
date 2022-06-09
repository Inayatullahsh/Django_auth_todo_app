from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from tasks.forms import TaskModelForm
from tasks.models import Task

from .forms import CreateUserForm

# Create your views here.


@login_required
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


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You're successfully registered!")
            login(request, user)
            return redirect('homepage')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in!")
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You've successfully logged in!")
                return redirect('homepage')
            else:
                messages.info(request, 'Username OR Password is incorrect!')
        return render(request, 'accounts/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homepage')
    else:
        return redirect('accounts:login')
