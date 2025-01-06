from rest_framework import serializers
from .models import Comment
from django.conf import settings


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
      return obj.user.username,


    class Meta:
        model = Comment
        fields = ('id','content', 'post', 'user', 'username')