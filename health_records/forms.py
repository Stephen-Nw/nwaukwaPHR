from django import forms
from django.forms import ModelForm
from .models import UserProfile


# Create a user profile form based on user profile model
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('relationship', 'prefix', 'first_name', 'last_name', 'date_of_birth', 'height_ft', 'height_in', 'weight_lbs', 'blood_type', 'address',
                  'email', 'phone', 'pcp', 'pcp_address', 'pcp_number', 'emergency_contact', 'emergency_phone')
        labels = {
            'prefix': 'Prefix', 'first_name': 'First Name', 'last_name': 'Last Name', 'date_of_birth': 'Date of Birth',
            'height_ft': 'Height(ft)', 'height_in': 'Height(in)', 'weight_lbs': 'Weight(lbs)', 'blood_type': 'Blood type',
            'address': 'Address', 'email': 'Email Address', 'phone': 'Phone Number', 'pcp': 'Primary Care Provider',
            'pcp_address': 'Provider Address', 'pcp_number': 'Provider Number', 'emergency_contact': 'Emergency Contact',
            'emergency_phone': 'Contact Phone', 'relationship': 'Relationship'
        }
