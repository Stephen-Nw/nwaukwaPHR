from re import A
from django.shortcuts import render, redirect
from .forms import UserProfileForm, AllergyProfileForm, MedicationProfileForm, AppointmentProfileForm, MedicalHistoryProfileForm, ImmunizationProfileForm, FamilySocialProfileForm


def homepage(request):
    return render(request, "health_records/index.html")


def user_profile(request):
    """Retrieves data from user profile form and save to db if POST request. 
    Displ;ay blank user profile form if GET request"""
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_medHx')
    else:
        form = UserProfileForm()
        return render(request, 'health_records/user_profile.html', {'form': form})


def user_medHx(request):
    form = MedicalHistoryProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('user_meds')
    else:
        form = MedicalHistoryProfileForm()
        return render(request, 'health_records/user_medHx.html', {'form': form})


def user_allergy(request):
    form = AllergyProfileForm()
    return render(request, 'health_records/user_allergy.html', {'form': form})


def user_meds(request):
    form = MedicationProfileForm()
    return render(request, "health_records/user_meds.html", {'form': form})


def user_appointments(request):
    form = AppointmentProfileForm()
    return render(request, 'health_records/user_appointments.html', {'form': form})


def user_immunization(request):
    form = ImmunizationProfileForm()
    return render(request, 'health_records/user_immunization.html', {'form': form})


def user_familySocialHx(request):
    form = FamilySocialProfileForm()
    return render(request, 'health_records/user_familySocialHx.html', {'form': form})
