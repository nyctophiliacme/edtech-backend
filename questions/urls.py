from django.urls import path
from questions.views import QuestionViewChapterVise

urlpatterns = [
    path('practice/', QuestionViewChapterVise.as_view()),
]