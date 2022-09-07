from django.shortcuts import render


def user_login(request):
    return render(request, 'authenticate/login.html')


def user_register(request):
    return render(request, 'authenticate/register_user.html')
