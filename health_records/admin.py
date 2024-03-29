from django.contrib import admin
from .models import MedicalHistoryProfile, UserProfile, AllergyProfile, MedicationProfile, AppointmentProfile, ImmunizationProfile, FamilySocialProfile

# Register your models here.
# admin.site.register(UserProfile)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'date_of_birth', 'email', 'phone')
    ordering = ('last_name', 'first_name')
    # list_filter = ('last_name',)
    search_fields = ('last_name', 'first_name')


@admin.register(AllergyProfile)
class AllergyProfileAdmin(admin.ModelAdmin):
    list_display = ('user_information', 'allergy_type', 'allergy_name',
                    'allergy_reaction', 'allergy_intervention', 'allergy_notes')
    ordering = ('allergy_type', 'allergy_reaction')
    search_fields = ('allergy_type',)


@admin.register(MedicationProfile)
class MedicationProfileAdmin(admin.ModelAdmin):
    list_display = ('user_information', 'med_name', 'med_indication', 'med_dosage',
                    'med_frequency', 'med_start', 'med_duration', 'med_ongoing')
    search_fields = ('med_name',)


@admin.register(AppointmentProfile)
class AppointmentProfileAdmin(admin.ModelAdmin):
    list_display = ('user_information', 'appt_date', 'appt_time', 'appt_provider',
                    'appt_address', 'appt_instructions')
    search_fields = ('appt_provider',)


@admin.register(MedicalHistoryProfile)
class MedicalHistoryProfileAdmin(admin.ModelAdmin):
    list_display = ('user_information', 'hx_type', 'hx_date', 'hx_diagnosis',
                    'hx_procedure', 'hx_medications', 'hx_notes')
    search_fields = ('hx_type',)


@admin.register(ImmunizationProfile)
class ImmunizationProfileAdmin(admin.ModelAdmin):
    list_display = ('user_information', 'vaccine_name', 'vaccine_date', 'vaccine_reaction',
                    'vaccine_rxn_if_positive', 'vaccine_next_due', 'vaccine_notes')
    search_fields = ('vaccine_name',)


@admin.register(FamilySocialProfile)
class FamilySocialProfileAdmin(admin.ModelAdmin):
    fields = ('status', ('smoker', 'smoker_duration', 'smoker_frequency'), ('alcohol',
                                                                            'alcohol_duration', 'alcohol_frequency'), ('drug', 'drug_names', 'drug_duration'))
    list_display = ('user_information', 'status', 'smoker', 'smoker_duration', 'smoker_frequency', 'alcohol',
                    'alcohol_duration', 'alcohol_frequency', 'drug', 'drug_names', 'drug_duration')
