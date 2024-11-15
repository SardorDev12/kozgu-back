from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from .serializers import RegisterSerializer
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class HomeView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterSerializer

    def get_object(self):
        return self.request.user
    
class LogoutView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, req):
        logout(req)
        return Response({'message': 'Logged out'}, status = status.HTTP_200_OK)
















class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(email=user)

class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer