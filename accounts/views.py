from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
# Create your views here.


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You'r account created successfully!")
            login(request, user)
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You'r already logged in!")
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "You've successfully logged in!")
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR Password is incorrect!')
        return render(request, 'accounts/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('accounts:login')
