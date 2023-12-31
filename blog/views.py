from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class Home(ListView):
    model = Post
    template_name = 'home.html'


class Post_page (DetailView):
    model = Post
    template_name = 'post_page.html'


class New(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


class Edit(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class Delete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
