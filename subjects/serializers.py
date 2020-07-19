from rest_framework import serializers

from subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    exam_code = serializers.CharField(source='exam.exam_code', read_only=True)

    class Meta:
        model = Subject
        fields = ('id', 'subject_code', 'title', 'description', 'image_url', 'exam_code', 'background_start_color',
                  'background_end_color')
