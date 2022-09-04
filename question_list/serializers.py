from rest_framework import serializers
from .models import QuestionList


class QuestionListSerializer(serializers.ModelSerializer):
    question_rel = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text',
    )

    class Meta:
        model = QuestionList
        fields = ('id', 'title', 'description', 'question_rel',)
