# admin.py
from django.contrib import admin
from .models import Category, Post, PostViews, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'category', 'title', 'author', 'published_at')
    list_filter = ('category', 'author')
    search_fields = ('title', 'author')

@admin.register(PostViews)
class PostViewsAdmin(admin.ModelAdmin):
    list_display = ('post_view_id', 'post', 'total_views')
    search_fields = ('post__title',)  # Use double underscore to navigate relationships

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'post', 'content', 'created_at')
    search_fields = ('post__title', 'content')  # Use double underscore to navigate relationships
