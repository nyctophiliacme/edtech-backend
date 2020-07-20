from subjects.models import Subject
from exams.models import Exam
from subjects.serializers import SubjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class SubjectView(APIView):

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SubjectSerializer(data=request.data)
        exam_obj = Exam.objects.get(exam_code=request.data.get("exam_code"))
        if serializer.is_valid():
            serializer.save(exam=exam_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectViewExamVise(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.filter(exam__exam_code=request.query_params.get("exam_code"))
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class SubjectViewCourseVise(APIView):

    def get(self, request, *args, **kwargs):
        exam_ids = Exam.objects.filter(course_id=request.query_params.get("course_id")).values_list(
            'id', flat=True)
        subjects = Subject.objects.filter(id__in=exam_ids).order_by('id')
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
