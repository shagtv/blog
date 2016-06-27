from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25], template_name='blog/blog.html'), name='index'),
    #url(r'^contact/', views.contact, name='contact'),
]
