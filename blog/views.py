from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView
# Create your views here.


class Home(ListView):
    model = Post
    template_name = 'home.html'
