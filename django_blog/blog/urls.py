from django.urls import path
from django.contrib.auth.views import LogoutView

from django_blog.blog.templates.blog.views import profile_view
from .views import profile_view
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:login'), name='logout'),
    path('profile/', profile_view, name='profile'),
]