from django.shortcuts import render
from .models import Detail_CV
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexClass(LoginRequiredMixin,views.View):
    login_url = '/user/login/'
    def get(self,request):
        return render(request,'detailCV/index.html',{"f":Detail_CV.objects.all()})