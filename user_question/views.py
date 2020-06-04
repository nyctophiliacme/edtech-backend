from user_question.serializers import UserQuestionProgressSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user_question.models import UserQuestionProgress


class UserQuestionProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            user_question_progress = UserQuestionProgress.objects.get(user_id=user_id,
                                                                      question_id=request.data.get('question'))
            serializer = UserQuestionProgressSerializer(user_question_progress, data=request.data)
        except UserQuestionProgress.DoesNotExist:
            serializer = UserQuestionProgressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
