from rest_framework import serializers

from exam_details.models import ExamSectionContainer, ExamSectionDetail


class ExamSectionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSectionDetail
        fields = ['id', 'section_title', 'section_html']


class ExamSectionContainerSerializer(serializers.ModelSerializer):
    section_details = ExamSectionDetailsSerializer(many=True, read_only=True, source='examsectiondetail_set')

    class Meta:
        model = ExamSectionContainer
        fields = ['id', 'section_container_title', 'section_details']
