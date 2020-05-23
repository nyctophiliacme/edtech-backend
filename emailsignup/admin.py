from django.contrib import admin

# Register your models here.
from django.contrib import admin
from emailsignup.models import CustomUser

admin.site.register(CustomUser)
