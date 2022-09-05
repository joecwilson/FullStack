from django.urls import path
from .views import QuestionGroupView
from django.views.generic import TemplateView

urlpatterns = [
    path("<int:pk>/", TemplateView.as_view(template_name='question_list.html'), name="react"),
    path("", QuestionGroupView.as_view(), name="home"),

]
