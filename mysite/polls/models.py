from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    questiontext = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def waspublishedrecently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.questiontext

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.CharField(max_length=200)
    choicetext = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choicetext) 