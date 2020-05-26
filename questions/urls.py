from django.urls import path
from questions.views import QuestionViewChapterVise, QuestionPostView

urlpatterns = [
    path('practice/', QuestionViewChapterVise.as_view()),
    path('save_data/', QuestionPostView.as_view())
]