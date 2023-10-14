"""
database
"""
from django.db import models

# Create your models here.

class Question(models.Model):
    """the question model

    Args:
        models (question_text): text of question
        models (pub_date): publication date
    """
    question_text:models.CharField = models.CharField(max_length=200)
    pub_date:models.DateTimeField = models.DateTimeField('date published')
    def __str__(self):
        try:
            return self.question_text
        except TypeError:
            return str(self.question_text)

class Choice(models.Model):
    """the choice model

    Args:
        models (question): the question link
        models (choice_text): text of choice
        models (votes): number of votes
    """
    question:models.ForeignKey = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text:models.CharField = models.CharField(max_length=200)
    votes:models.IntegerField = models.IntegerField(default=0)
    def __str__(self):
        try:
            return self.choice_text
        except TypeError:
            return str(self.choice_text)
