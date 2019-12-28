from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     any_feedback = models.CharField(max_length=200,blank=True)
#     votes = models.IntegerField(default=0)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username



class Rating(models.Model):
    choice = [(1, '1'),(2, '2'), (3, '3'), (4, '4'), (5, '5')]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_rated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice = models.IntegerField(choices=choice,default=2)
    feedback = models.TextField(blank=True)
    rated_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        text=self.question.question_text+" was rated by "+self.user_rated.username+" and given "+str(self.choice)+" points."
        return text