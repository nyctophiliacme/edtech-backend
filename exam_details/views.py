from exam_details.models import ExamSectionContainer, ExamSectionDetail
from exams.models import Exam
from exam_details.serializers import ExamSectionContainerSerializer, ExamSectionDetailsSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ExamSectionContainerView(APIView):

    def get(self, request, *args, **kwargs):
        exam_section_containers = ExamSectionContainer.objects.all().order_by('id')
        serializer = ExamSectionContainerSerializer(exam_section_containers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ExamSectionContainerSerializer(data=request.data)
        exam_obj = Exam.objects.get(exam_code=request.data.get("exam_code"))

        if serializer.is_valid():
            serializer.save(exam=exam_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamSectionContainerExamViseView(APIView):

    def get(self, request, *args, **kwargs):
        exam_section_containers = ExamSectionContainer.objects.filter(
            exam_id=request.query_params.get('exam_id')).order_by('id')
        serializer = ExamSectionContainerSerializer(exam_section_containers, many=True)
        return Response(serializer.data)


class ExamSectionDetailsView(APIView):

    def get(self, request, *args, **kwargs):
        exam_section_details = ExamSectionDetail.objects.all().order_by('id')
        serializer = ExamSectionDetailsSerializer(exam_section_details, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ExamSectionDetailsSerializer(data=request.data)
        exam_section_container_obj = ExamSectionContainer.objects.get(id=request.data.get("exam_section_container_id"))

        if serializer.is_valid():
            serializer.save(exam_section_container=exam_section_container_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamSectionDetailsContainerViseView(APIView):

    def get(self, request, *args, **kwargs):
        exam_section_details = ExamSectionDetail.objects.filter(
            exam_section_container_id=request.query_params.get('exam_section_container_id')).order_by('id')
        serializer = ExamSectionDetailsSerializer(exam_section_details, many=True)
        return Response(serializer.data)
