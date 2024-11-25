from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    parents_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(default="", max_length=300)
    profile_pic_url = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.username}"
