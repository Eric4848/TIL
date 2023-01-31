from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('var01/', views.variable01),
    path('var02/', views.variable02),
    path('for/', views.testfor),
    path('if01/', views.if01),
    path('if02/', views.if02),
]