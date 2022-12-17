from django.urls import path
from . import views

urlpatterns = [
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_allergy', views.user_allergy, name='user_allergy'),
    path('user_meds', views.user_meds, name='user_meds'),
    path('user_appointments', views.user_appointments, name='user_appointments'),
    path('user_medHx', views.user_medHx, name='user_medHx'),
    path('user_immunization', views.user_immunization, name='user_immunization'),
    path('user_test', views.user_test, name='user_test'),
    path('user_familySocialHx', views.user_familySocialHx,
         name='user_familySocialHx'),
]


# TODO: Add slug to user_allergy because user may have multiple allergies
# TODO: Add slug to user_meds because user may have multiple meds
