from dataclasses import fields
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email', 'username','password']

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        return token
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email', 'username','password']
    
    def validate(self, attrs):
        if CustomUser.objects.filter(username=attrs['username']):
            raise serializers.ValidationError("This user has already registered.")

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['username'])
        user.save()

        return user

        