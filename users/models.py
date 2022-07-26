from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NewUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_address = models.EmailField()
