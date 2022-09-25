from django.db import models
from django.utils import timezone


class QuestionList(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
