from django.urls import path
from courses.views import CourseView

urlpatterns = [
    path('get_all/', CourseView.as_view()),
]
