from django.contrib import admin
from django.urls import path
from str_backend.views import PostListCreate, CommentListCreate

urlpatterns = [
    path('encry/', admin.site.urls),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
