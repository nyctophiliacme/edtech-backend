from rest_framework import serializers

from help_request.models import HelpRequest


class HelpRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = HelpRequest
        fields = ('id', 'user_first_name', 'user_email', 'message', 'is_guest_user', 'created_on', 'modified_at')
