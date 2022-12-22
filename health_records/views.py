from re import A
from django import forms
from django.shortcuts import render, redirect
from .forms import UserProfileForm, AllergyProfileForm, MedicationProfileForm, AppointmentProfileForm, MedicalHistoryProfileForm, ImmunizationProfileForm, FamilySocialProfileForm
from .models import MedicalHistoryProfile, UserProfile
from django.contrib.auth.decorators import login_required


def user_test(request):
    med_hx = MedicalHistoryProfile.objects.all()
    return render(request, 'health_records/user_test.html', {"med_hx": med_hx})


@login_required
def user_profile(request):
    """Retrieves data from user profile form and save to db if POST request. 
    Display blank user profile form if GET request"""
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_medHx')
    else:
        form = UserProfileForm()
        return render(request, 'health_records/user_profile.html', {'form': form})


@login_required
def user_medHx(request):
    if request.method == "POST":
        form = MedicalHistoryProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_meds')
    else:
        form = MedicalHistoryProfileForm()
        return render(request, 'health_records/user_medHx.html', {'form': form})


@login_required
def user_meds(request):
    if request.method == "POST":
        form = MedicationProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_allergy')
    else:
        form = MedicationProfileForm()
        return render(request, "health_records/user_meds.html", {'form': form})


@login_required
def user_allergy(request):
    if request.method == "POST":
        form = AllergyProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_familySocialHx')
    else:
        form = AllergyProfileForm()
        return render(request, 'health_records/user_allergy.html', {'form': form})


@login_required
def user_familySocialHx(request):
    if request.method == "POST":
        form = FamilySocialProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_immunization')
    else:
        form = FamilySocialProfileForm()
        return render(request, 'health_records/user_familySocialHx.html', {'form': form})


@login_required
def user_immunization(request):
    if request.method == "POST":
        form = ImmunizationProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_test')
    else:
        form = ImmunizationProfileForm()
        return render(request, 'health_records/user_immunization.html', {'form': form})


@login_required
def user_appointments(request):
    form = AppointmentProfileForm()
    return render(request, 'health_records/user_appointments.html', {'form': form})


# TODO: Add login required to views
