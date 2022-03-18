from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from natijaapp.models import *
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Foydalanuvchi
from quizapp.models import Quiz, Savol, Javob
class ResultView(View):
    def get(self, request):
        marks = Foydalanuvchi.objects.all()
        return render(request, 'results.html', {'marks':marks})
class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self,request):
        user=User.objects.create_user(
            username=request.POST['username'],
            password=request.POST.get('password1'),
        )
        login(request, user)
        return redirect('index')
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request, username=usern, password=passw)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('index')
def logoutView(request):
    logout(request)
    return redirect('login')

