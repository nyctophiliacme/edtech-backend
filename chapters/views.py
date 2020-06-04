from chapters.models import Chapter
from chapters.serializers import ChapterSerializer
from exams.models import Exam
from subjects.models import Subject
from user_question.models import UserQuestionProgress

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ChapterView(APIView):

    def get(self, request, *args, **kwargs):
        chapters = Chapter.objects.all().order_by('id')
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ChapterSerializer(data=request.data)
        exam_obj = Exam.objects.get(exam_code=request.data.get("exam_code"))
        subject_obj = Subject.objects.get(subject_code=request.data.get("subject_code"), exam=exam_obj)

        if serializer.is_valid():
            serializer.save(exam=exam_obj, subject=subject_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapterViewSubjectExamVise(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        chapters = Chapter.objects.filter(exam__exam_code=request.query_params.get("exam_code"),
                                          subject__subject_code=request.query_params.get("subject_code")).order_by('id')
        serializer = ChapterSerializer(chapters, many=True)

        for chapter_data in serializer.data:
            chapter_data['user_total_attempts'] = UserQuestionProgress.objects.filter(
                user_id=user_id, chapter_id=chapter_data['id']).count()

            chapter_data['user_correct_attempts'] = UserQuestionProgress.objects.filter(
                user_id=user_id, chapter_id=chapter_data['id'], is_correctly_solved=True).count()

        return Response(serializer.data)
