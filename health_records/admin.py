from django.contrib import admin
from .models import UserProfile, AllergyProfile, MedicationProfile

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
    list_display = ('allergy_type', 'allergy_name',
                    'allergy_reaction', 'allergy_intervention', 'allergy_notes')
    ordering = ('allergy_type', 'allergy_reaction')
    search_fields = ('allergy_type',)


@admin.register(MedicationProfile)
class MedicationProfileAdmin(admin.ModelAdmin):
    list_display = ('med_name', 'med_indication', 'med_dosage',
                    'med_frequency', 'med_start', 'med_duration', 'med_ongoing')
    search_fields = ('med_name',)
