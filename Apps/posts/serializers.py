from rest_framework import serializers

from ..tags.models import Tag
from .models import Post
from ..categories.models import Category


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
            'created_at',
            'updated_at',
            'status'

        ]

    category = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Category.objects.all()
    )

    
    tag = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )