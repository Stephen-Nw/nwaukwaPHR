from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """New user registration form"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
