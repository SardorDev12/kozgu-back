from .models import PostImages
from .serializers import postImagesSerializer
from rest_framework import generics

class PostImageCreateRetrieveAPIView(generics.ListCreateAPIView):
    queryset = PostImages.objects.all()
    serializer_class = postImagesSerializer
    
