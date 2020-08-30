from django.db import models
from chapters.models import Chapter
from emailsignup.models import CustomUser


class Question(models.Model):
    question_text = models.TextField()
    question_title = models.TextField(blank=True, null=True)
    question_type = models.CharField(blank=True, null=True, max_length=100)
    question_img_url = models.TextField(blank=True, null=True)

    difficulty_level = models.CharField(max_length=50, choices=(
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult')), default='moderate', db_index=True)

    time_to_solve = models.IntegerField(blank=True, null=True)
    answer_selection_type = models.CharField(max_length=50, default='single_choice', db_index=True)
    explanation = models.TextField(blank=True, null=True)
    explanation_img_url = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'id': self.pk,
            'question_title': self.question_title,
            'question_text': self.question_text,
            'question_type': self.question_type,
            'question_img_url': self.question_img_url,
            'difficulty_level': self.difficulty_level,
            'time_to_solve': self.time_to_solve,
            'answer_selection_type': self.answer_selection_type,
            'explanation': self.explanation,
            'explanation_img_url': self.explanation_img_url,
        }


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    choice_img_url = models.TextField(blank=True, null=True)
    is_right_choice = models.BooleanField(default=False)

    class Meta:
        ordering = ['pk']


class QuestionChapterMapping(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('question', 'chapter'),)


class QuestionBugReport(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bug_title = models.TextField(blank=True, null=True)
    bug_description = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
