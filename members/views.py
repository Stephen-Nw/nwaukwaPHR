from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout

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
        return redirect('home_login')
    context = {'form': form}
    return render(request, 'members/user_register.html', context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(
            request, ("You have been logged out. Please close your browser window."))
        return redirect('home_login')
    return render(request, 'members/logout.html')


# TODO: Format Logout form
