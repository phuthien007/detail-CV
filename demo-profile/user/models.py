from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    telephone= models.CharField(max_length=15)
    address=models.CharField(max_length=100)
