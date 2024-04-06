# views.py
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Post, Comment, Category
from .serializers import PostSerializer, PostPreviewSerializer1, PostPreviewSerializer2, PostPreviewSerializer3, CommentSerializer, CategorySerializer, EmailListSerializer, PostSerializer2
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
        serializer = PostSerializer2(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_post_views(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.total_views += 1
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
    queryset = Post.objects.all().order_by('?')[:3]
    serializer_class = PostPreviewSerializer1

#most read
# fields = ['title','img_url','author','published_at','slug']
class PostPreview2(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-total_views')[:10]
    serializer_class = PostPreviewSerializer2

# fields = ['title','img_url','author','summary','slug']
class PostPreview3(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-post_id')[:12]
    serializer_class = PostPreviewSerializer3

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@api_view(['GET'])
def get_posts_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = category.posts.all()
    serializer = PostPreviewSerializer3(posts, many=True)  
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request):
    if request.method == 'POST':
        post_id = request.data.get('post_id')
        content = request.data.get('content')
        
        if not post_id or not content:
            return Response({'error': 'Both post_id and content are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        post = get_object_or_404(Post, pk=post_id)
        serializer = CommentSerializer(data={'post': post_id, 'content': content})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_comments(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class PostSearchAPIView(generics.ListAPIView):
    serializer_class = PostPreviewSerializer3

    def get_queryset(self):
        query = self.request.query_params.get('query', '').lower()  # Convert query to lowercase
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | 
                Q(author__icontains=query) | 
                Q(tags__icontains=query)
            )
        return Post.objects.none()