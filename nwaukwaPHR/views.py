from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def home_login_view(request):
    """Renders hompage and user login form"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_profile')
        else:
            messages.success(
                request, ("Your username and/or password is incorrect. Please try again."))
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "health_records/index.html", context)


# TODO: Format previously logged in notification - Red, Bold
