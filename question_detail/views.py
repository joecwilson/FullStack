from .models import Question
from rest_framework import generics
from .serializers import QuestionSerializer


# Create your views here.
class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
