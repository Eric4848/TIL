"""mymember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("register/", views.register, name='register'),
    # Login/Logout
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # django가 가지고있는 로그인/로그아웃
    # get: login.html/ post: 객체 저장 후 보내줌
    # settings.py LOGIN_REDIRECT_URL='/result' 로그인 시 /result로 이동
    path('result/', views.result, name='result'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # settings.py LOGOUT_REDIRECT_URL='/' 로그아웃 시 /로 이동
]
