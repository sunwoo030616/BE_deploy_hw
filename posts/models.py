from django.db import models

# Create your models here.
# Post 클래스 생성
class Post(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title