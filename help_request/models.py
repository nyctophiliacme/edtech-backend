from django.db import models
from emailsignup.models import CustomUser
from commons.custom_email import send_help_request_email


class HelpRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    is_guest_user = models.BooleanField(default=True)
    user_first_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    message = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(HelpRequest, self).save(*args, **kwargs)
        send_help_request_email(user_name=self.user_first_name, is_guest_user=self.is_guest_user,
                                user_email=self.user_email, message=self.message)
