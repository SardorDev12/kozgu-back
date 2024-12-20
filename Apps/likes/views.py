from .serializers import LikeSerializer
from rest_framework import generics
from .models import Like
from rest_framework.permissions import AllowAny

class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]

    
class LikeRetrieveView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]


class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeUndoView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
