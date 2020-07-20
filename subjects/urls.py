from django.urls import path
from subjects.views import SubjectView, SubjectViewExamVise, SubjectViewCourseVise

urlpatterns = [
    path('', SubjectView.as_view()),
    path('exam_vise/', SubjectViewExamVise.as_view()),
    path('course_vise/', SubjectViewCourseVise.as_view()),
]
