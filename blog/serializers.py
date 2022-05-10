from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    posts_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'posts_number')


class PostQuantitySerializer(serializers.Serializer):
    date = serializers.DateField()
    posts_number = serializers.IntegerField(read_only=True)
