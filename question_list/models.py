from django.db import models
from question_detail.models import Question


class QuestionList(models.Model):
    title = models.CharField(max_length=1500)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
