# views.py
from rest_framework import generics
from .models import Post, Comment, Category
from .serializers import PostSerializer, PostPreviewSerializer1, PostPreviewSerializer2, CommentSerializer, CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# fields = ['title','author','published_at']
class PostPreview1(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPreviewSerializer1

# fields = ['title','img_url','author','published_at']
class PostPreview2(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPreviewSerializer2

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
