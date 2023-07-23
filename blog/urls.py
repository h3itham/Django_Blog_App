from django.urls import path
from .views import Home, Post_page, New, Edit

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/', Post_page.as_view(), name='post_page'),
    path('newpost/', New.as_view(), name='newpost'),
    path('post/<int:pk>/edit/', Edit.as_view(), name='post_edit')
]
