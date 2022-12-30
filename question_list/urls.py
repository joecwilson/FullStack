from django.urls import path
from .views import QuestionGroupView, QuestionListCreateView
from django.views.generic import TemplateView

app_name = 'question_list'
urlpatterns = [
    path("<int:pk>/", TemplateView.as_view(template_name='question_list.html'), name="react"),
    path("create_new/", QuestionListCreateView.as_view(), name="new group"),
    path("", QuestionGroupView.as_view(), name="home"),

]
