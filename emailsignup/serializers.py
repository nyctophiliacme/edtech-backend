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

    current_class = serializers.CharField(required=False)
    school = serializers.CharField(required=False)
    city = serializers.CharField(required=False)

    date_of_birth = serializers.DateField(required=False)

    parent_name = serializers.CharField(required=False)
    parent_email = serializers.CharField(required=False)
    parent_phone_number = serializers.CharField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),

            'current_class': self.validated_data.get('current_class', ''),
            'school': self.validated_data.get('school', ''),
            'city': self.validated_data.get('city', ''),

            'date_of_birth': self.validated_data.get('date_of_birth', ''),

            'parent_name': self.validated_data.get('parent_name', ''),
            'parent_email': self.validated_data.get('parent_email', ''),
            'parent_phone_number': self.validated_data.get('parent_phone_number', ''),
        }

    def custom_signup(self, request, user):
        phone_number = self.validated_data.get('phone_number', '')
        current_class = self.validated_data.get('current_class', '')
        school = self.validated_data.get('school', '')
        city = self.validated_data.get('city', '')

        date_of_birth = self.validated_data.get('date_of_birth', '')
        parent_name = self.validated_data.get('parent_name', '')
        parent_email = self.validated_data.get('parent_email', '')
        parent_phone_number = self.validated_data.get('parent_phone_number', '')

        if phone_number:
            user.phone_number = phone_number
        if current_class:
            user.current_class = current_class
        if school:
            user.school = school
        if city:
            user.city = city
        if date_of_birth:
            user.date_of_birth = date_of_birth
        if parent_name:
            user.parent_name = parent_name
        if parent_email:
            user.parent_email = parent_email
        if parent_phone_number:
            user.parent_phone_number = parent_phone_number

        user.save(update_fields=['phone_number', 'current_class', 'school', 'city', 'date_of_birth', 'parent_name',
                                 'parent_email', 'parent_phone_number'])


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'first_name', 'last_name', 'phone_number', 'current_class', 'school', 'city',
                  'date_of_birth', 'parent_name', 'parent_email', 'parent_phone_number']
