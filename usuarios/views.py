from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView 

# Create your views here.
class UserLogin(SuccessMessageMixin, LoginView):
	template_name = 'login.html'

