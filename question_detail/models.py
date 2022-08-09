from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=1000)
    answer = models.DecimalField(decimal_places=3, max_digits=13)
