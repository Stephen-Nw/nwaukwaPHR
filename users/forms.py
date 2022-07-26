from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser


class NewUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = "___all__"
