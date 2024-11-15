from django.db import models
from django.conf import settings

class Profile(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field="username")
    bio = models.TextField(default="", max_length=300)
    profile_pic_url = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user_id.username}"
