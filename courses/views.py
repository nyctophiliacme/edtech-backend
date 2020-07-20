from courses.models import CourseContainer, Course
from courses.serializers import CourseContainerSerializer, CourseExamSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        courses = CourseContainer.objects.all().order_by('id')
        serializer = CourseContainerSerializer(courses, many=True)

        return Response(serializer.data)


class ExamCourseViseView(APIView):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseExamSerializer(courses, many=True)
        return Response(serializer.data)
