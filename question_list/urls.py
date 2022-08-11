from django.urls import path
from .views import QuestionGroupView


urlpatterns = [
    path("", QuestionGroupView.as_view(), name="home"),
]
