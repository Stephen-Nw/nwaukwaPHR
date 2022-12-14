from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def user_login(request):
    return render(request, 'accounts/login.html')


def user_register(request):
    '''Render blank registration form if no user info provided. Add new user to db if registration form is filled and valid.'''
    # form = UserCreationForm(request.POST or None)
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'accounts/user_register.html', context)
