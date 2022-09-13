from django import forms
from django.forms import ModelForm
from .models import UserProfile, AllergyProfile


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
        widgets = {
            'prefix': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'height_ft': forms.TextInput(attrs={'class': 'form-control'}),
            'height_in': forms.TextInput(attrs={'class': 'form-control'}),
            'weight_lbs': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'pcp_address': forms.TextInput(attrs={'class': 'form-control'}),
            'pcp_number': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'pcp': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AllergyProfileForm(ModelForm):
    class Meta:
        model = AllergyProfile
        fields = ('allergy_type', 'allergy_reaction',
                  'allergy_intervention', 'allergy_notes')
        labels = {
            'allergy_type': 'Type',
            'allergy_name': 'Allergic Substance',
            'allergy_reaction': 'Allergic Reaction',
            'allergy_intervention': 'Intervention/Treatment (Optional)',
            'allergy_notes': 'Additional Notes',
        }
