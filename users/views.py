from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm

# Create your views here.


def register(request):
    """New user registration form"""
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data
            form.save()
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})
