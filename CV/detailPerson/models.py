from django.db import models


# Create your models here.
class person(models.Model):
    fullname = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tel=models.CharField(max_length=100)
    def __str__(self):
        return self.fullname