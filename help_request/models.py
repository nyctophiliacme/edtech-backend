from django.db import models
from emailsignup.models import CustomUser


class HelpRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    is_guest_user = models.BooleanField(default=True)
    user_first_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    message = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
