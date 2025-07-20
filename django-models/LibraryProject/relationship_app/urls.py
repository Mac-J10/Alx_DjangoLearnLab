from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view

app_name = 'relationship_app'

urlpatterns = [
    # Existing book and library views…
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Authentication views
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),
]