from django.views.generic import ListView
from .models import QuestionList
# Create your views here.


class QuestionGroupView(ListView):
    model = QuestionList
    template_name = 'index.html'
