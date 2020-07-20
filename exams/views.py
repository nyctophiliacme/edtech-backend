from exams.models import Exam
from exams.serializers import ExamSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ExamView(APIView):

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamCourseIdViseView(APIView):

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.filter(course_id=request.query_params.get("course_id"))
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)
