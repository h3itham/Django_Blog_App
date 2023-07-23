from django.urls import path
from .views import Home, Post_page, New

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/', Post_page.as_view(), name='post_page'),
    path('newpost/', New.as_view(), name='newpost'),
]
