from django.shortcuts import render
from education.models import Education
from detailPerson.models import person
from project.models import Project, detailProject
from django import views


# Create your views here.
class IndexClass(views.View):
    def get(self, request):
        edu = Education.objects.all()
        per = person.objects.all()
        pro = Project.objects.all()
        return render(request, 'disploy/home.html', {'per': per, 'edu':edu,'pro':pro})

class ProjectClass(views.View):
    def get(self,request):
        de=detailProject.objects.all()
        return render(request,'disploy/project.html',{'de':de} )