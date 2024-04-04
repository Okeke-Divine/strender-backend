# admin.py
from django.contrib import admin
from .models import Category, Post, Comment, EmailList

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name','img_url')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'category', 'title', 'author', 'published_at')
    list_filter = ('category', 'author')
    search_fields = ('title', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'post', 'content', 'created_at')
    search_fields = ('post__title', 'content')  # Use double underscore to navigate relationships

admin.site.register(EmailList)