from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


def user_login(request):
    return render(request, 'members/login.html')


def user_register(request):
    '''Render blank registration form if no user info provided. Add new user to db if registration form is filled and valid.'''
    # form = UserCreationForm(request.POST or None)
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(
            request, ("You have been successfully registered. Please log in"))
        return redirect('homepage-info')
    context = {'form': form}
    return render(request, 'members/user_register.html', context)
