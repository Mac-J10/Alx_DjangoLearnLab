# blog/urls.py

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    profile_view,
    register_view,
    login_view,
)
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    # Post CRUD
    path('posts/', PostListView.as_view(),            name='post_list'),
    path('post/new/', PostCreateView.as_view(),       name='post_create'),      # post/new/
    path('post/<int:pk>/', PostDetailView.as_view(),  name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # post/<int:pk>/update/
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # post/<int:pk>/delete/

    # Profile & Auth
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view,     name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:login'), name='logout'),
]