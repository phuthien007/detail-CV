from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class detailProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Role = models.CharField(max_length=100)
    Funding = models.CharField(max_length=100)
    ProjectTitle = models.CharField(max_length=100)
    MainArea = models.CharField(max_length=100)
    def __str__(self):
        return self.project.name