from django.db import models


class CourseContainer(models.Model):
    course_container_title = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'id': self.pk,
            'course_container_title': self.course_container_title,
        }

    class Meta:
        ordering = ['pk']


class Course(models.Model):
    course_container = models.ForeignKey(CourseContainer, on_delete=models.CASCADE)
    course_title = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pk']
