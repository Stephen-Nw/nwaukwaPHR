from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser


class NewUserForm(UserCreationForm):
    user_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = NewUser
        fields = ("user_name", "first_name", "last_name",
                  "email", "password1", "password2")
