from django.urls import reverse_lazy
from django.views.generic import CreateView
from question_list.models import QuestionList
from .forms import CustomUserCreationForm
from django.views.generic import ListView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class ProfileView(ListView):
    model = QuestionList
    template_name = 'profiles.html'

    def get_queryset(self):
        return QuestionList.objects.filter(author=self.request.user)
