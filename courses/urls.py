from django.urls import path
from courses.views import CourseView, ExamCourseViseView

urlpatterns = [
    path('get_all/', CourseView.as_view()),
    path('exams/', ExamCourseViseView.as_view()),
]
