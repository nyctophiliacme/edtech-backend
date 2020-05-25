from questions.models import Question, QuestionChoice, QuestionChapterMapping
from questions.serializers import QuestionSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class QuestionViewChapterVise(APIView):

    def get(self, request, *args, **kwargs):
        chapter_id = request.query_params.get('chapter_id')
        question_ids = QuestionChapterMapping.objects.filter(chapter_id=chapter_id).values_list('pk', flat=True)

        questions = Question.objects.filter(question_id__in=question_ids)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
