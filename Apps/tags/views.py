
from .models import Tag
from .serializers import TagSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDeleteView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
