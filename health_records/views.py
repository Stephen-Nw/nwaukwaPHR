from django.shortcuts import render
from .forms import UserProfileForm

# Create your views here.


def homepage(request):
    return render(request, "health_records/index.html")


def user_profile(request):
    form = UserProfileForm()
    return render(request, 'user_profile.html', {'form': form})
