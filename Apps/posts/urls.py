# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='Post'),
    path('posts/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
