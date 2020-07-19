from rest_framework import serializers

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
