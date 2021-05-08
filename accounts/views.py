from django.shortcuts import redirect, render

from .forms import CreateUserForm
# Create your views here.


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def login_view(request):
    pass


def logout_view(request):
    pass
