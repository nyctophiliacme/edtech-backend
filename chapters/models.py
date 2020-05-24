from django.db import models
from exams.models import Exam
from subjects.models import Subject


class Chapter(models.Model):
    chapter_code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    is_locked = models.BooleanField(default=True)
    question_count = models.IntegerField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('chapter_code', 'subject'),)

    def to_json(self):
        return {
            'id': self.pk,
            'chapter_code': self.chapter_code,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'subject': self.subject_id,
            'exam': self.exam_id,
            'is_locked': self.is_locked,
            'question_count': self.question_count,
        }
