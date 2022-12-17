from django.urls import path
# from members.views import (
#     user_login,
#     user_register,
# )
from . import views

app_name = 'members'

urlpatterns = [
    path('user_register', views.user_register, name='register'),

]
