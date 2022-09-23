from re import A
from django.shortcuts import render
from .forms import UserProfileForm, AllergyProfileForm, MedicationProfileForm, AppointmentProfileForm, MedicalHistoryProfileForm


def homepage(request):
    return render(request, "health_records/index.html")


def user_profile(request):
    form = UserProfileForm()
    return render(request, 'health_records/user_profile.html', {'form': form})


def user_allergy(request):
    form = AllergyProfileForm()
    return render(request, 'health_records/user_allergy.html', {'form': form})


def user_meds(request):
    form = MedicationProfileForm()
    return render(request, "health_records/user_meds.html", {'form': form})


def user_appointments(request):
    form = AppointmentProfileForm()
    return render(request, 'health_records/user_appointments.html', {'form': form})


def user_medHx(request):
    form = MedicalHistoryProfileForm()
    return render(request, 'health_records/user_medHx.html', {'form': form})


def user_immunization(request):
    return render(request, 'health_records/user_immunization.html')
