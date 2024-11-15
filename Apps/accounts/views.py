from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer