import datetime

from django.contrib.auth.models import User
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import PostFilter
from .models import Post
from .serializers import PostSerializer, UserSerializer, PostQuantitySerializer


class PostViewSet(viewsets.ModelViewSet):
    """COMMENT 13052022"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter

    @action(methods=['get'], detail=False)
    def get_user_posts(self, request):
        qs = UserSerializer(data=User.objects.annotate(posts_number=Count('posts')), many=True)
        qs.is_valid()
        return Response(qs.data)

    @action(methods=['get'], detail=False)
    def get_posts_by_date(self, request):
        qs = Post.objects.all().values('date').annotate(posts_number=Count('id'))
        filtered_qs = self.filter_queryset(qs)
        serializer = PostQuantitySerializer(data=filtered_qs, many=True)
        serializer.is_valid()
        return Response(serializer.data)
