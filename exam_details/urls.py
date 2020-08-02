from django.urls import path
from exam_details.views import ExamSectionContainerExamViseView, ExamSectionContainerView, \
    ExamSectionDetailsContainerViseView, ExamSectionDetailsView

urlpatterns = [
    path('section_container', ExamSectionContainerView.as_view()),
    path('section_container/exam_vise/', ExamSectionContainerExamViseView.as_view()),
    path('section_details', ExamSectionDetailsContainerViseView.as_view()),
    path('section_details/container_vise/', ExamSectionDetailsView.as_view()),
]
