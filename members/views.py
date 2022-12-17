from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# There is no separate user login template, view, or url.
# This is because the homepage and the user login form are on the same template.
# Look for user login logic "health_records.views"


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
