from rest_framework import serializers

from questions.models import Question, QuestionChoice


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ['id', 'choice_text', 'choice_img_url', 'is_right_choice']


class QuestionSerializer(serializers.ModelSerializer):
    question_choice = QuestionChoiceSerializer(many=True, read_only=True, source='question_choice_set')

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_title', 'question_type', 'question_img_url', 'difficulty_level',
                  'time_to_solve', 'answer_selection_type', 'explanation', 'explanation_img_url', 'question_choice']
