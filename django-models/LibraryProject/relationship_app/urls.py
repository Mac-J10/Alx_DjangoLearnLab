from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books


app_name = 'relationship_app'

urlpatterns = [
    # existing app views
    path('books/', list_books, name='book-list'),
    path('books/', views.list_books, name='book-list'),

    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # registration view
    path('register/', views.register, name='register'),

    # login/logout using built-in class-based views with custom templates
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
]