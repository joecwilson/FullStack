from django.db import models
from question_list.models import QuestionList


class Question(models.Model):
    text = models.CharField(max_length=1000)
    answer = models.DecimalField(decimal_places=3, max_digits=13)
    question_group = models.ForeignKey(QuestionList, related_name='question_rel', on_delete=models.CASCADE)
    position = models.IntegerField()
    default_visibility = models.IntegerField()

    def __str__(self):
        return self.text
