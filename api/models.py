from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=20)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = [phone_number]

    def __str__(self):
        return self.username

