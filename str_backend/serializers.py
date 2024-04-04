# serializers.py
from rest_framework import serializers
from .models import Post, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'img_url','total_posts']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostPreviewSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author', 'published_at', 'slug']


class PostPreviewSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'img_url', 'author', 'published_at', 'slug']


class PostPreviewSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'img_url', 'author', 'summary', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
