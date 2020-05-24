from rest_framework import serializers

from exams.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'code', 'title', 'description', 'image_url')
