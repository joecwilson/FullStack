from django.views.generic import ListView
from .models import QuestionList
from rest_framework import viewsets
from .serializers import QuestionListSerializer

# Create your views here.


class QuestionGroupView(ListView):
    model = QuestionList
    template_name = 'index.html'


# Create your views here.

class QuestionListAPI(viewsets.ModelViewSet):
    serializer_class = QuestionListSerializer
    queryset = QuestionList.objects.all()
