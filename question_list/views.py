from django.views.generic import ListView
from .models import QuestionList
from rest_framework import viewsets, generics
from .serializers import QuestionListSerializer


class QuestionGroupView(ListView):
    model = QuestionList
    template_name = 'index.html'


class ListQuestionList(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = QuestionList.objects.all()


class DetailQuestionList(generics.RetrieveAPIView):
    serializer_class = QuestionListSerializer
    queryset = QuestionList.objects.all()
