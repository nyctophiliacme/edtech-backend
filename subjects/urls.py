from django.urls import path
from subjects.views import SubjectView

urlpatterns = [
    path('', SubjectView.as_view()),
]
