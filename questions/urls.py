from django.urls import path
from questions.views import QuestionViewChapterVise, QuestionPostView, QuestionBugReportView

urlpatterns = [
    path('practice/', QuestionViewChapterVise.as_view()),
    path('save_data/', QuestionPostView.as_view()),
    path('bug_report/', QuestionBugReportView.as_view()),
]
