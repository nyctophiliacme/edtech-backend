from rest_framework import serializers

from chapters.models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    subject_code = serializers.CharField(source='subject.subject_code', read_only=True)
    exam_code = serializers.CharField(source='exam.exam_code', read_only=True)

    class Meta:
        model = Chapter
        fields = ('id', 'chapter_code', 'title', 'description', 'image_url', 'subject_code', 'exam_code', 'is_locked',
                  'question_count')
