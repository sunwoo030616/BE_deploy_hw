from django.shortcuts import render
from .models import Post
from rest_framework import viewsets, mixins

# Post 클래스의 모든 객체를 가져와서 PostSerializer로 변환
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response

class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer