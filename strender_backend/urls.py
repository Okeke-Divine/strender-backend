from django.contrib import admin
from django.urls import path
from str_backend.views import CategoryListAPIView, PostListCreate, CommentListCreate

urlpatterns = [
    path('encry/', admin.site.urls),
    path('api/v1/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/v1/posts/', PostListCreate.as_view(), name='post-list-create'),
    path('api/v1/comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
