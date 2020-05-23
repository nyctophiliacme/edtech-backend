from django.views import View
from exams.models import Exam
from exams.serializers import ExamSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ExamView(View):

    @api_view(['GET'])
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            exams = Exam.objects.all()
            serializer = ExamSerializer(exams, many=True)
            return Response(serializer.data)

    @api_view(['POST'])
    def post(self, request, *args, **kwargs):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
