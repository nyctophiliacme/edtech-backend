from django.urls import path
from exam_details.views import ExamSectionContainerExamViseView, ExamSectionContainerView, \
    ExamSectionDetailsContainerViseView, ExamSectionDetailsView

urlpatterns = [
    path('section_container/', ExamSectionContainerView.as_view()),
    path('section_container_exam_vise/', ExamSectionContainerExamViseView.as_view()),
    path('section_details/', ExamSectionDetailsView.as_view()),
    path('section_details_container_vise/', ExamSectionDetailsContainerViseView.as_view()),
]
