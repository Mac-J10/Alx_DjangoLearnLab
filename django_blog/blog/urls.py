# blog/urls.py

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,    
    CommentUpdateView,
    CommentDeleteView,
    register_view,
    login_view,
    profile_view,
)
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    # … your existing post URLs …
    path('posts/', PostListView.as_view(),             name='post_list'),
    path('post/new/', PostCreateView.as_view(),        name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(),   name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs – ADD THESE:
    path(
        'post/<int:pk>/comments/new/',
        CommentCreateView.as_view(),
        name='comment_create'
    ),  # handles POST/new comment on a specific post

    path(
        'comment/<int:pk>/update/',
        CommentUpdateView.as_view(),
        name='comment_update'
    ),  # edit an existing comment

    path(
        'comment/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment_delete'
    ),  # delete an existing comment

    # Authentication & Profile
    path('register/', register_view, name='register'),
    path('login/',    login_view,    name='login'),
    path('logout/',   LogoutView.as_view(next_page='blog:login'), name='logout'),
    path('profile/',  profile_view,  name='profile'),
]