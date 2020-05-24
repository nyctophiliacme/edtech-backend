from django.urls import path
from chapters.views import ChapterView, ChapterViewSubjectExamVise

urlpatterns = [
    path('', ChapterView.as_view()),
    path('subject_vise/', ChapterViewSubjectExamVise.as_view())
]