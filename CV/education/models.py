from django.db import models


# Create your models here.
class Education(models.Model):
    yearStart = models.DateField("started")
    yearFinish = models.DateField("finished")
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
