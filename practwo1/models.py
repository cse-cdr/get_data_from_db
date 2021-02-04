from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published Date')

    def __str__(self):
        return self.question.__str__()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

class Choice(models.Model):
    question_str = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_str = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_str.__str__()