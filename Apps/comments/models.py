from django.db import models
from ..posts.models import Post
from django.conf import settings



class Comment(models.Model):
    content = models.TextField(default='')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, to_field='title')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)