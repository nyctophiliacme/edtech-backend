from rest_framework import serializers

from subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    exam_code = serializers.CharField(source='exam.code', read_only=True)

    class Meta:
        model = Subject
        fields = ('id', 'code', 'title', 'description', 'image_url', 'exam_code')
