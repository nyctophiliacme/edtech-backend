from rest_framework import serializers

from courses.models import Course, CourseContainer
from exams.models import Exam


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_title']


class CourseContainerSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True, source='course_set')

    class Meta:
        model = CourseContainer
        fields = ['id', 'course_container_title', 'courses']


class ExamCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_code', 'title', 'description', 'image_url']


class CourseExamSerializer(serializers.ModelSerializer):
    exams = ExamCustomSerializer(many=True, read_only=True, source='exam_set')

    class Meta:
        model = Course
        fields = ['id', 'course_title', 'exams']
