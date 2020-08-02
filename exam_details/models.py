from django.db import models
from exams.models import Exam


class ExamSectionContainer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    section_container_title = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'id': self.pk,
            'section_title': self.section_container_title,
        }

    class Meta:
        ordering = ['pk']


class ExamSectionDetail(models.Model):
    exam_section_container = models.ForeignKey(ExamSectionContainer, on_delete=models.CASCADE)
    section_title = models.TextField()
    section_html = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pk']
