from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage-info'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_allergy', views.user_allergy, name='user_allergy'),
    path('user_meds', views.user_meds, name='user_meds'),
]


# TODO: Add slug to user_allergy because user may have multiple allergies
# TODO: Add slug to user_meds because user may have multiple meds
