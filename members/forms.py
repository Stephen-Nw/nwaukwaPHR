from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        labels = {
            'Username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': ' Email Address',
            'password1': 'Password',
            'password2': 'Re-enter Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }