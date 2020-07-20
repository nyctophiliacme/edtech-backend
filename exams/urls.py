from django.urls import path
from exams.views import ExamView, ExamCourseIdViseView

urlpatterns = [
    path('', ExamView.as_view()),
    path('course_vise', ExamCourseIdViseView.as_view())
]