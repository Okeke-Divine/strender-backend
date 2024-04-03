# views.py
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
