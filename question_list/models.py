from django.db import models


class QuestionList(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()

    def __str__(self):
        return self.title
