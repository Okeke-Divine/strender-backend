from django.contrib import admin
from django.urls import path
from str_backend.views import CategoryListAPIView, PostListCreate, CommentListCreate, PostPreview1, PostPreview2, PostPreview3, add_email

urlpatterns = [
    path('encry/', admin.site.urls),
    path('api/v1/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/v1/posts/', PostListCreate.as_view(), name='post-list-create'),
    path('api/v1/posts-preview/type-1/', PostPreview1.as_view(), name='post-preview-type-1'),
    path('api/v1/posts-preview/type-2/', PostPreview2.as_view(), name='post-preview-type-2'),
    path('api/v1/posts-preview/type-3/', PostPreview3.as_view(), name='post-preview-type-3'),
    path('api/v1/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('api/v1/add_email/', add_email, name='create_email'),
]
