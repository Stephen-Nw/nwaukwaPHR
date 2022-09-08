from django import forms
from django.forms import ModelForm
from .models import UserProfile


# Create a user profile form based on user profile model
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'date_of_birth', 'height_ft', 'height_in', 'weight_lbs', 'blood_type', 'address',
                  'email', 'phone', 'pcp', 'pcp_address', 'pcp_number', 'emergency_contact', 'emergency_phone', 'relationship')
