from questions.models import Question, QuestionChoice, QuestionChapterMapping
from questions.serializers import QuestionSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class QuestionViewChapterVise(APIView):

    def get(self, request, *args, **kwargs):
        chapter_id = request.query_params.get('chapter_id')
        question_ids = QuestionChapterMapping.objects.filter(chapter_id=chapter_id).values_list('question_id', flat=True)

        questions = Question.objects.filter(id__in=question_ids)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionPostView(APIView):

    def post(self, request, *args, **kwargs):
        self.save_question_data(request.data)

    @staticmethod
    def save_question_data(data):
        serializer = QuestionSerializer(data=data)

        if serializer.is_valid():
            try:
                question = serializer.save()
                # Save Question Choices
                for i in range(1, 5):
                    question_choice_get = "question_choice_" + str(i)
                    if i == int(data.get("correct_choice")):
                        QuestionChoice.objects.create(
                            choice_text=data.get(question_choice_get),
                            is_right_choice=True,
                            question=question
                        )
                    else:
                        QuestionChoice.objects.create(
                            choice_text=data.get(question_choice_get),
                            question=question
                        )
                # Save Question Chapter Mapping
                QuestionChapterMapping.objects.create(question=question, chapter_id=data.get("chapter_id"))

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as err:
                print("Exception occurred in Question Post \n", err)
        print("Exception in Question Post\n", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

