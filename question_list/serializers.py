from rest_framework import serializers
from .models import QuestionList
from question_detail.serializers import QuestionSerializer


class QuestionListSerializer(serializers.ModelSerializer):
    question_rel = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionList
        fields = ('id', 'title', 'description', 'question_rel',)
