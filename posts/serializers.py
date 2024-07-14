from rest_framework import serializers
from .models import Post

# PostSerializer 클래스 생성
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    