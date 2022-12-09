from django.shortcuts import render


def user_login(request):
    return render(request, 'accounts/login.html')


def user_register(request):
    return render(request, 'accounts/register_user.html')
