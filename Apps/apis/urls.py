from django.urls import path
from ..posts.views import PostDeleteView, PostListView,PostCreateView, PostUpdateView, PostRetrieveView
from ..categories.views import CategoryListView,CategoryCreateView, CategoryDeleteView, CategoryUpdateView, CategoryRetrieveView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='Posts'),
    path('posts/create/', PostCreateView.as_view(), name='Post Create'),
    path('posts/<int:pk>/', PostRetrieveView.as_view(), name='Post Retrieve'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='Post Update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='Post Delete'),

    path('categories/', CategoryListView.as_view(), name='Categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='Categories Create'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='Categories Retrieve'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='Categories Update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='Categories Delete'),
]


