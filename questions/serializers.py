from rest_framework import serializers

from questions.models import Question, QuestionChoice


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ['id', 'choice_text', 'choice_img_url', 'is_right_choice']


class QuestionSerializer(serializers.ModelSerializer):
    question_choice = QuestionChoiceSerializer(many=True, read_only=True, source='questionchoice_set')
    user_question_choice_id = serializers.IntegerField(read_only=True)
    user_attempt_is_correct = serializers.BooleanField(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_title', 'question_type', 'question_img_url', 'difficulty_level',
                  'time_to_solve', 'answer_selection_type', 'explanation', 'explanation_img_url', 'question_choice',
                  'user_question_choice_id', 'user_attempt_is_correct']
