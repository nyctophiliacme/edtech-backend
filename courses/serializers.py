from rest_framework import serializers

from exams.serializers import ExamSerializer
from courses.models import Course, CourseContainer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_title']


class CourseContainerSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True, source='course_set')

    class Meta:
        model = CourseContainer
        fields = ['id', 'course_container_title', 'courses']


class CourseExamSerializer(serializers.ModelSerializer):
    exams = ExamSerializer(many=True, read_only=True, source='exam_set')

    class Meta:
        model = Course
        fields = ['id', 'course_title', 'exams']
