from django.contrib import admin
from django.urls import path, include
from usuarios.views import (UserLogin)

from django.contrib.auth.views import (
	PasswordResetDoneView,
)


urlpatterns = [
	path('login/', UserLogin.as_view(), name='login'), 
	path('', include('django.contrib.auth.urls')),
]