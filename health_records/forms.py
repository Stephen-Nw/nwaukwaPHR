from django import forms
from django.forms import ModelForm
from .models import MedicalHistoryProfile, MedicationProfile, UserProfile, AllergyProfile, AppointmentProfile


# Create a user appointment form based on the user appointment model
class AppointmentProfileForm(ModelForm):
    class Meta:
        model = AppointmentProfile
        fields = ('appt_date', 'appt_time', 'appt_provider',
                  'appt_address', 'appt_instructions')
        labels = {
            'appt_date': 'Date',
            'appt_time': 'Time',
            'appt_provider': 'Provider',
            'appt_address': 'Address',
            'appt_instructions': 'Additional Instructions',
        }
        widgets = {
            'appt_date': forms.DateInput(attrs={'class': 'form-control'}),
            'appt_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'appt_provider': forms.TextInput(attrs={'class': 'form-control'}),
            'appt_address': forms.TextInput(attrs={'class': 'form-control'}),
            'appt_instructions': forms.Textarea(attrs={'class': 'form-control'}),
        }


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


# Create an allergy profile form based on the allergy profile model
class AllergyProfileForm(ModelForm):
    class Meta:
        model = AllergyProfile
        fields = ('allergy_type', 'allergy_reaction', 'allergy_name',
                  'allergy_intervention', 'allergy_notes')
        labels = {
            'allergy_type': 'Type',
            'allergy_name': 'Allergic Substance',
            'allergy_reaction': 'Allergic Reaction',
            'allergy_intervention': 'Intervention/Treatment (Optional)',
            'allergy_notes': 'Additional Notes',
        }
        widgets = {
            'allergy_type': forms.Select(attrs={'class': 'form-control'}),
            'allergy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'allergy_reaction': forms.TextInput(attrs={'class': 'form-control'}),
            'allergy_intervention': forms.Textarea(attrs={'class': 'form-control'}),
            'allergy_notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


# Create a medication profile form based on the medication profile model
class MedicationProfileForm(ModelForm):
    class Meta:
        model = MedicationProfile
        fields = ('med_name', 'med_indication', 'med_dosage',
                  'med_frequency', 'med_start', 'med_duration', 'med_ongoing')
        labels = {
            'med_name': 'Medication Name',
            'med_indication': 'Clinical Indication',
            'med_dosage': 'Dosage',
            'med_frequency': 'Frequency',
            'med_start': 'Start Date',
            'med_duration': 'Duration',
            'med_ongoing': 'Currently Taking',
        }
        widgets = {
            'med_name': forms.TextInput(attrs={'class': 'form-control'}),
            'med_indication': forms.TextInput(attrs={'class': 'form-control'}),
            'med_dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'med_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'med_start': forms.TextInput(attrs={'class': 'form-control'}),
            'med_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'med_ongoing': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class MedicalHistoryProfileForm(ModelForm):
    class Meta:
        model = MedicalHistoryProfile
        fields = ('hx_type', 'hx_date', 'hx_diagnosis',
                  'hx_procedure', 'hx_medications', 'hx_notes')
        labels = {
            'hx_type': 'Type',
            'hx_date': 'Date',
            'hx_diagnosis': 'Diagnosis',
            'hx_procedure': 'Procedure',
            'hx_medications': 'Medications',
            'hx_notes': 'Additional Notes'
        }
        widgets = {
            'hx_type': forms.Select(attrs={'class': 'form-control'}),
            'hx_date': forms.DateInput(attrs={'class': 'form-control'}),
            'hx_diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'hx_procedure': forms.TextInput(attrs={'class': 'form-control'}),
            'hx_medications': forms.TextInput(attrs={'class': 'form-control'}),
            'hx_notes': forms.Textarea(attrs={'class': 'form-control'})
        }
