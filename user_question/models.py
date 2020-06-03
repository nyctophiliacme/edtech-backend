from django.db import models
from exams.models import Exam
from subjects.models import Subject
from chapters.models import Chapter
from emailsignup.models import CustomUser
from questions.models import Question, QuestionChoice


class UserQuestionProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    is_correctly_solved = models.BooleanField(default=False)

    time_taken_to_solve = models.IntegerField(null=True, blank=True)

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'question'),)

    def save(self, *args, **kwargs):
        super(UserQuestionProgress, self).save(*args, **kwargs)
        UserQuestionProgressLog.objects.create(user_question_progress=self, question_choice=self.question_choice,
                                               is_correctly_solved=self.is_correctly_solved,
                                               time_taken_to_solve=self.time_taken_to_solve)


class UserQuestionProgressLog(models.Model):
    user_question_progress = models.ForeignKey(UserQuestionProgress, on_delete=models.CASCADE)
    question_choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    is_correctly_solved = models.BooleanField(default=False)
    time_taken_to_solve = models.IntegerField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
