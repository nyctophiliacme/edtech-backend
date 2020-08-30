from questions.models import Question, QuestionChoice, QuestionChapterMapping, QuestionBugReport
from questions.serializers import QuestionSerializer, QuestionBugReportSerializer
from user_question.models import UserQuestionProgress

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class QuestionViewChapterVise(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        chapter_id = request.query_params.get('chapter_id')
        question_ids = QuestionChapterMapping.objects.filter(chapter_id=chapter_id).values_list(
            'question_id', flat=True)

        questions = Question.objects.filter(id__in=question_ids).order_by('id')
        serializer = QuestionSerializer(questions, many=True)

        for question_data in serializer.data:
            try:
                user_question_attempt = UserQuestionProgress.objects.get(user_id=user_id,
                                                                         question_id=question_data['id'])
                question_data['user_question_choice_id'] = user_question_attempt.question_choice_id
                question_data['user_attempt_is_correct'] = user_question_attempt.is_correctly_solved

            except UserQuestionProgress.DoesNotExist:
                question_data['user_question_choice_id'] = None
                question_data['user_attempt_is_correct'] = None

        return Response(serializer.data)


class QuestionPostView(APIView):

    def post(self, request, *args, **kwargs):
        return self.save_question_data(request.data)

    @staticmethod
    def save_question_data(data):
        serializer = QuestionSerializer(data=data)

        if serializer.is_valid():
            try:
                question = serializer.save()
                # Save Question Choices
                for i in range(1, 5):
                    question_choice_get = "question_choice_" + str(i)
                    choice_img_url = "question_choice_" + str(i) + "_image_url"
                    if i == int(data.get("correct_choice")):
                        QuestionChoice.objects.create(
                            choice_text=data.get(question_choice_get),
                            choice_img_url=data.get(choice_img_url),
                            is_right_choice=True,
                            question=question
                        )
                    else:
                        QuestionChoice.objects.create(
                            choice_text=data.get(question_choice_get),
                            choice_img_url=data.get(choice_img_url),
                            question=question
                        )
                # Save Question Chapter Mapping
                QuestionChapterMapping.objects.create(question=question, chapter_id=data.get("chapter_id"))

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as err:
                print("Exception occurred in Question Post \n", err)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        print("Exception in Question Post\n", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionBugReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        question_bugs = QuestionBugReport.objects.all()
        serializer = QuestionBugReportSerializer(question_bugs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        user_id = request.user.id
        serializer = QuestionBugReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
