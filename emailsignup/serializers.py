from rest_framework import serializers

from emailsignup.models import CustomUser
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    city = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'city': self.validated_data.get('city', ''),
            'date_of_birth': self.validated_data.get('date_of_birth', ''),
        }

    def custom_signup(self, request, user):
        if self.validated_data.get('phone_number', ''):
            user.phone_number = self.validated_data.get('phone_number', '')

        if self.validated_data.get('city', ''):
            user.city = self.validated_data.get('city', '')

        if self.validated_data.get('date_of_birth', ''):
            user.date_of_birth = self.validated_data.get('date_of_birth', '')

        user.save(update_fields=['phone_number', 'city', 'date_of_birth'])


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'city']


