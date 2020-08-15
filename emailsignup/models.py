from django.db import models
from django.contrib.auth.models import AbstractUser

from emailsignup.managers import CustomUserManager

from django.dispatch import receiver
from django.db.models.signals import pre_save


class CustomUser(AbstractUser):

    objects = CustomUserManager()

    phone_number = models.CharField(blank=True, max_length=30)
    current_class = models.CharField(blank=True, null=True, max_length=10)
    school = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    is_paid_user = models.BooleanField(default=False)

    is_superteacher_admin = models.BooleanField(default=False, blank=True, null=True)

    parent_name = models.CharField(blank=True, null=True, max_length=255)
    parent_email = models.CharField(blank=True, null=True, max_length=255)
    parent_phone_number = models.CharField(blank=True, null=True, max_length=30)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


@receiver(pre_save, sender=CustomUser)
def update_username_from_email(sender, instance, **kwargs):
    instance.username = instance.email