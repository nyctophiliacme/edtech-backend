from courses.models import CourseContainer
from courses.serializers import CourseContainerSerializer, CourseExamSerializer
from exams.models import Exam

from rest_framework.response import Response
from rest_framework.views import APIView


class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        courses = CourseContainer.objects.all().order_by('id')
        serializer = CourseContainerSerializer(courses, many=True)

        return Response(serializer.data)


class ExamCourseViseView(APIView):

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.filter(course_id=request.query_params.get("course_id"))
        serializer = CourseExamSerializer(exams, many=True)
        return Response(serializer.data)
