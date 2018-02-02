
from django.db import models
from django.conf import settings


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class userdetails(models.Model):
    UserID = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    FirstName  = models.CharField(max_length=200)
    Secondname = models.CharField(max_length=200)
    Age = models.IntegerField(default=18)
    Voted =  models.BooleanField(default=False)
    def __str__(self):
        return self.FirstName + " " + self.Secondname
