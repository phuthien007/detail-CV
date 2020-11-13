from django.shortcuts import render,HttpResponse
from django import views
from django.contrib.auth import login,authenticate
# Create your views here.

class Login(views.View):
    def get(self,request):
        return render(request,'user/login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        my_user=authenticate(username=username,password=password)
        if my_user is None:
            return HttpResponse('failed')
        login(request,my_user)
        return HttpResponse('Congratulation')