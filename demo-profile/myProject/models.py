from django.db import models


# Create your models here.
class Project(models.Model):
    nameProject = models.CharField(max_length=100)
    dateTime = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
