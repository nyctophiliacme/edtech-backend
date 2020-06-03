from django.urls import path
from user_question.views import UserQuestionProgressView

urlpatterns = [
    path('question_answered/', UserQuestionProgressView.as_view())
]
