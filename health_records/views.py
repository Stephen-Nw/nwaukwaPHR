from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "health_records/index.html")


def user_profile(request):
    return render(request, 'user_profile.html')
