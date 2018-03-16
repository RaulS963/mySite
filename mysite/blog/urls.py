from django.contrib import admin
from django.urls import path , include
from . import views
from django.views.generic import ListView , DetailView
from blog.models import Post

urlpatterns = [
    path('', views.main , name='main' ),
	path('personal/', views.personal , name='personal' ),
	path('about/', views.about , name='about' ),
	path('blog-list/', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="list.html")),
	
]
