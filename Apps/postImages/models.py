from django.db import models
from django.conf import settings
from Apps.posts.models import Post

class PostImages(models.Model):
    post_image = models.ImageField(upload_to='article_pics', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

