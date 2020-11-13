from django.db import models
from user.models import MyUser


# Create your models here.
class University(models.Model):
    nameUni = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    CPA = models.FloatField(default=0)
    time_at_started = models.DateTimeField()
    time_at_finished = models.DateTimeField()


class Education(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
