from rest_framework import serializers

from user_question.models import UserQuestionProgress


class UserQuestionProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserQuestionProgress
        fields = '__all__'
        exclude = ['created_on', 'modified_at']
