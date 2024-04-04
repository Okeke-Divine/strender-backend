# views.py
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Comment, Category
from .serializers import PostSerializer, PostPreviewSerializer1, PostPreviewSerializer2, PostPreviewSerializer3, CommentSerializer, CategorySerializer, EmailListSerializer
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@api_view(['POST'])
def add_email(request):
    serializer = EmailListSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email address'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def update_post_views(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views_count += 1
    post.save()
    return JsonResponse({'message': 'Post views updated successfully'})

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('?')
    serializer_class = CategorySerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('?')
    serializer_class = PostSerializer

# fields = ['title','author','published_at','slug']
class PostPreview1(generics.ListAPIView):
    queryset = Post.objects.all().order_by('?')
    serializer_class = PostPreviewSerializer1

# fields = ['title','img_url','author','published_at','slug']
class PostPreview2(generics.ListAPIView):
    queryset = Post.objects.all().order_by('?')
    serializer_class = PostPreviewSerializer2

# fields = ['title','img_url','author','summary','slug']
class PostPreview3(generics.ListAPIView):
    queryset = Post.objects.all().order_by('?')
    serializer_class = PostPreviewSerializer3

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('?')
    serializer_class = CommentSerializer
