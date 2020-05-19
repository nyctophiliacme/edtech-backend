from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    objects = CustomUserManager()

    phone_number = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
