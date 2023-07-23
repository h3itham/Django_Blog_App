from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView, DetailView
# Create your views here.


class Home(ListView):
    model = Post
    template_name = 'home.html'


class Post_page (DetailView):
    model = Post
    template_name = 'post_page.html'
