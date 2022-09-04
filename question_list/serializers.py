from rest_framework import serializers
from .models import QuestionList


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionList
        fields = ('id', 'title', 'description',)
