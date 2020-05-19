from rest_framework import serializers

from emailsignup.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'city']
