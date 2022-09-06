from django.shortcuts import render


def user_login(request):
    return render(request, 'authenticate/login.html')
