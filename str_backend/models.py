from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    img_url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.PROTECT, null=False)
    title = models.CharField(max_length=200, null=False)
    img_url = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=50, null=True)
    summary = models.TextField(null=False, default='')
    content = models.TextField(null=False, default='')
    slug = models.CharField(max_length=50, null=False)
    tags = models.CharField(max_length=200, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostViews(models.Model):
    post_view_id = models.AutoField(primary_key=True)
    post = models.OneToOneField(Post, related_name='views', on_delete=models.CASCADE, default=0)
    total_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=0)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content