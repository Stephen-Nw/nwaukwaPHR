from django.urls import path
# from members.views import (
#     user_login,
#     user_register,
# )
from . import views

app_name = 'members'

urlpatterns = [
    path('user_login', views.user_login, name='login'),
    path('user_register', views.user_register, name='register'),

]
