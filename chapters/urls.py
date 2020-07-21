from django.urls import path
from chapters.views import ChapterView, ChapterViewSubjectExamVise, ChapterViewSubjectExamViseGuestUser

urlpatterns = [
    path('', ChapterView.as_view()),
    path('subject_vise/', ChapterViewSubjectExamVise.as_view()),
    path('subject_vise_guest/', ChapterViewSubjectExamViseGuestUser.as_view()),
]
