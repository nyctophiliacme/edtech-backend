from django.urls import path
from exams.views import ExamView

urlpatterns = [
    path('', ExamView.as_view()),
]