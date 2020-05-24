from django.db import models
from exams.models import Exam


class Subject(models.Model):
    subject_code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('subject_code', 'exam'),)

    def to_json(self):
        return {
            'id': self.pk,
            'subject_code': self.subject_code,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'exam': self.exam_id
        }
