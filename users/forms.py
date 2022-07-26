from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUserData


class NewUserForm(UserCreationForm):
    class Meta:
        model = NewUserData
        fields = "___all__"
