from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class QuestionList(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1500)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=1000)
    answer = models.DecimalField(decimal_places=3, max_digits=13)
    question_group = models.ForeignKey(QuestionList, related_name='question_rel', on_delete=models.CASCADE)
    position = models.IntegerField()
    visible = models.IntegerField()

    def __str__(self):
        return self.text
