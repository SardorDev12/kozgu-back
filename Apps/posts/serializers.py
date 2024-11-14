from rest_framework import serializers
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
            'created_at',
            'updated_at',
            'status'

        ]

    category = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Category.objects.all()
    )