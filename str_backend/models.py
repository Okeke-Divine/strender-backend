from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250) 

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=50, default='')
    summary = models.CharField(max_length=200, null=True)
    content = models.TextField(default='')
    slug = models.CharField(max_length=50, default='')
    published_at = models.DateTimeField(auto_now_add=True)

class PostViews(models.Model):
    post_view_id = models.AutoField(primary_key=True)
    post = models.OneToOneField(Post, related_name='views', on_delete=models.CASCADE)
    total_views = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
