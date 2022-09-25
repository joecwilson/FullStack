from rest_framework import serializers
from .models import QuestionList, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'answer', 'position', 'visible')


class QuestionListSerializer(serializers.ModelSerializer):
    question_rel = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionList
        fields = ('id', 'title', 'description', 'question_rel',)
