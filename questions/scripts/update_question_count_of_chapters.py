import django
import os
import sys

sys.path.append("/home/ubuntu/edtech-backend")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superteacher.settings')
django.setup()

from exams.models import Exam
from subjects.models import Subject
from chapters.models import Chapter
from questions.models import QuestionChapterMapping

if __name__ == '__main__':
    exam = Exam.objects.get(exam_code=sys.argv[1])
    subjects = Subject.objects.filter(exam=exam)

    for subject in subjects:
        chapters = Chapter.objects.filter(subject=subject)
        for chapter in chapters:
            chapter.question_count = QuestionChapterMapping.objects.filter(chapter=chapter).count()
            chapter.save()
