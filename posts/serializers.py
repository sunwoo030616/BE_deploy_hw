from rest_framework import serializers
from .models import Post

# PostSerializer 클래스 생성
class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
    
    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y년 %m월 %d일')
    
