from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    return render(request, 'accounts/login.html')


def user_register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'accounts/register_user.html', context)
