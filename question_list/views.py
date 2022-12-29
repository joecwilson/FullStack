from django.views.generic import ListView
from .models import QuestionList
from rest_framework import viewsets, generics
from .serializers import QuestionListSerializer
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class QuestionGroupView(ListView):
    model = QuestionList
    template_name = 'index.html'


class ListQuestionList(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    queryset = QuestionList.objects.all()


class DetailQuestionList(generics.RetrieveAPIView):
    serializer_class = QuestionListSerializer
    queryset = QuestionList.objects.all()


class QuestionListCreateView(LoginRequiredMixin, CreateView):
    model = QuestionList
    template_name = 'create_questions.html'
    fields = ['title', 'description' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')
