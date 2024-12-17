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
        token['username'] = user.username
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email

        return data
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username','password']
        extra_kwargs = {'password': {'write_only': True}}
    
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

        