from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUserData


class NewUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()

    class Meta:
        model = NewUserData
        fields = ['first_name', 'last_name']
