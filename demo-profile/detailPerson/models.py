from django.db import models


# Create your models here.
class DetailPerson(models.Model):
    fullname = models.CharField(max_length=100)
    apply = models.CharField(max_length=100)
    dateofbirth = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
