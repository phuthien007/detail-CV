from django.shortcuts import render
from .models import person
from django import views
# Create your views here.

class Contact(views.View):
    def get(self,request):
        return render(request,'contact.html',{"p":person.objects.all})