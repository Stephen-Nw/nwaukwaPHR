from django.urls import path
from members.views import (
    user_login,
    user_register,
)

app_name = 'members'

urlpatterns = [
    path('user_login', user_login, name='login'),
    path('user_register', user_register, name='register'),

]
