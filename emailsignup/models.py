from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    objects = CustomUserManager()

    phone_number = models.CharField(blank=True, max_length=30)
    current_class = models.CharField(blank=True, null=True, max_length=10)
    school = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    is_paid_user = models.BooleanField(default=False)

    parent_name = models.CharField(blank=True, null=True, max_length=255)
    parent_email = models.CharField(blank=True, null=True, max_length=255)
    parent_phone_number = models.CharField(blank=True, null=True, max_length=30)

    def __str__(self):
        return self.email
