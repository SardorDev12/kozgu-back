from .serializers import LikeSerializer
from rest_framework import generics
from .models import Like
from rest_framework.permissions import IsAuthenticated

class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Like.objects.filter(user_id=user)
    
class LikeRetrieveView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Like.objects.filter(user_id=user)

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeUndoView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
