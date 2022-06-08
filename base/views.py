from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


# Create your views here.


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You'r account created successfully!")
            login(request, user)
            return redirect('homepage')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You'r already logged in!")
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
