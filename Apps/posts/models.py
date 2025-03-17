from django.db import models
from ..categories.models import Category
from django.conf import settings
from ..tags.models import Tag


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('published', 'Published'),
    ]


    title = models.CharField(max_length=200,unique=True)
    content = models.TextField(default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name' )
    tag = models.ManyToManyField(Tag, related_name="posts", default=['New'])
    read_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    article_pic = models.ImageField(upload_to='article_pics', default='article_pics/default.jpg')




    def __str__(self):
        return self.title
