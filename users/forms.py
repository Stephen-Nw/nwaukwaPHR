from django import forms
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
