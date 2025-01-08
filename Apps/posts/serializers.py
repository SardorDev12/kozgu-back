from rest_framework import serializers

from ..tags.models import Tag
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author',
            'category',
            'tag',
            'read_time',
            'created_at',
            'updated_at',
            'status',
            'article_pic',
            'published_at'

        ]


    
    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )