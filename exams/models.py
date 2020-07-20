from django.db import models
from courses.models import Course


class Exam(models.Model):
    exam_code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'id': self.pk,
            'code': self.code,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
        }
