from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class NewUserData(models.Model):
#     user_name = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email_address = models.EmailField(max_length=50)
#     password1 = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)


class NewUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USERNAME_FIELD = "username"
