from django.shortcuts import render
from django import views
# Create your views here.
class Login(views.View):
    def get(self, request, *args, **kwargs):
        return render(request,'login.html')

    def post(self, request, *args, **kwargs):
        return render(request,'login.html')
        
class Signup(views.View):
    def get(self, request, *args, **kwargs):
        return render(request,'signup.html')

    def post(self, request, *args, **kwargs):
        return render(request,'signup.html')
    
class Dashboard(views.View):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')

    def post(self, request, *args, **kwargs):
        return render(request,'index.html')
        