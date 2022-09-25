from django.contrib import admin
from .models import QuestionList, Question
# Register your models here.

admin.site.register(QuestionList)
admin.site.register(Question)
