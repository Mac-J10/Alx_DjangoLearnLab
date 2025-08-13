from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'blog'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:login'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
        path(
        'posts/<int:post_pk>/comments/new/',
        CommentCreateView.as_view(),
        name='comment_create'
    ),
    path(
        'posts/<int:post_pk>/comments/<int:pk>/edit/',
        CommentUpdateView.as_view(),
        name='comment_update'
    ),
    path(
        'posts/<int:post_pk>/comments/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment_delete'
    ),

]