from django.db import models


class Exam(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'id': self.id,
            'code': self.code,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
        }
