from django.db import models
from ..posts.models import Post
from django.conf import settings



class Comment(models.Model):
    content = models.TextField(default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # No need for `to_field`
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # Standard ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)