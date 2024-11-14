from django.db import models
from django.contrib.auth.models import User
from ..posts.models import Post

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,to_field='username')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    