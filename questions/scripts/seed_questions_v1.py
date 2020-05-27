import csv
import django
import os
import sys

sys.path.append("/home/ubuntu/edtech-backend")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superteacher.settings')
django.setup()
from questions.views import QuestionPostView

file_path = '/home/ubuntu/edtech-backend/questions/questions_csvs/' + sys.argv[1]
with open(file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        question_dict = {
            'question_text': row['question_text'],
            'question_img_url': row['question_img_url'],
            'difficulty_level': row['difficulty_level'],
            'explanation': row['explanation'],
            'explanation_img_url': row['explanation_img_url'],
            'chapter_id': row['chapter_id'],
            'question_choice_1': row['question_choice_1'],
            'question_choice_2': row['question_choice_2'],
            'question_choice_3': row['question_choice_3'],
            'question_choice_4': row['question_choice_4'],
            'correct_choice': row['correct_choice']
        }
        request = {
            'data': question_dict
        }
        question_post_view_obj = QuestionPostView()
        question_post_view_obj.post(request=request)
