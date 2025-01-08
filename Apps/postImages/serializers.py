from rest_framework import serializers
from .models import PostImages

class postImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = "__all__"