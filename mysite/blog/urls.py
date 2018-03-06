from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.main , name='main' ),
	path('personal/', views.personal , name='personal' ),
	path('about/', views.about , name='about' ),
	
]
