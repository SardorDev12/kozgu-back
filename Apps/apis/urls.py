from django.urls import path
from ..posts.views import PostDeleteView, PostListView,PostCreateView, PostUpdateView, PostRetrieveView
from ..categories.views import CategoryListView,CategoryCreateView, CategoryDeleteView, CategoryUpdateView, CategoryRetrieveView
from ..likes.views import LikeListView, LikeCreateView, LikeUndoView, LikeRetrieveView
from ..comments.views import CommentRetrieveView, CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView
from ..profiles.views import ProfileCreateView, ProfileListView, ProfileRetrieveUpdateDestroyView
from ..accounts.views import RegisterView, UserInfoView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ..tags.views import TagCreateView, TagDeleteView, TagRetrieveView, TagUpdateView, TagListView
from ..postImages.views import PostImageCreateRetrieveAPIView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='Posts'),
    path('posts/create/', PostCreateView.as_view(), name='Post Create'),
    path('posts/<int:pk>/', PostRetrieveView.as_view(), name='Post Retrieve'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='Post Update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='Post Delete'),
    path('post/<int:pk>/images/', PostImageCreateRetrieveAPIView.as_view(), name='post images create retrieve'),

    path('categories/', CategoryListView.as_view(), name='Categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='Categories Create'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='Categories Retrieve'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='Categories Update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='Categories Delete'),

    path('likes/', LikeListView.as_view(), name='Likes'),
    path('likes/<int:pk>/', LikeRetrieveView.as_view(), name='Like'),
    path('likes/create/', LikeCreateView.as_view(), name='Like Create'),
    path('likes/delete/<int:pk>/', LikeUndoView.as_view(), name='Like Undo'),

    path('posts/<int:pk>/comments/', CommentListView.as_view(), name='Comments'),
    path('comments/<int:pk>/', CommentRetrieveView.as_view(), name='Comment'),
    path('comments/create/', CommentCreateView.as_view(), name='Comment Create'),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='Comment Update'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='Comment Delete'),

    path('profiles/', ProfileListView.as_view(), name='profile-list-create'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),

    path('tags/', TagListView.as_view(), name='Tags'),
    path('tags/create/', TagCreateView.as_view(), name='Tags Create'),
    path('tags/<int:pk>/', TagRetrieveView.as_view(), name='Tags Retrieve'),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name='Tags Update'),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name='Tags Delete'),

    path('login/', TokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/',  RegisterView.as_view(), name='register'),
    path('user/',  UserInfoView.as_view(), name='register'),
]
