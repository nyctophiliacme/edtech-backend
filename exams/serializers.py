from rest_framework import serializers

from exams.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.course_title', read_only=True)

    class Meta:
        model = Exam
        fields = ('id', 'exam_code', 'title', 'description', 'image_url', 'course', 'course_title')
