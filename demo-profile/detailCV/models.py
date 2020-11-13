from django.db import models
from user.models import MyUser
from detailPerson.models import DetailPerson
from education.models import Education
from myProject.models import Project


# Create your models here.
class Detail_CV(models.Model):
    detailperson = models.ForeignKey(DetailPerson, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
