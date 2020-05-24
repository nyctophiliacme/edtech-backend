from django.urls import path
from subjects.views import SubjectView, SubjectViewExamVise

urlpatterns = [
    path('', SubjectView.as_view()),
    path('/exam_vise', SubjectViewExamVise.as_view())
]
