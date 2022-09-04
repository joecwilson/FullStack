from django.urls import path
from .views import ListQuestionList, DetailQuestionList

urlpatterns = [
    path("<int:pk>/", DetailQuestionList.as_view(), name="question_list_detail"),
    path("", ListQuestionList.as_view(), name="question_list_list"),
]
