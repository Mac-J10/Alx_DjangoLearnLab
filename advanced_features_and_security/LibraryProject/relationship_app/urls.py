from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books


app_name = 'relationship_app'

urlpatterns = [
    path('add_book/', views.add_book, name='book-add'),
    path('edit_book/<int:pk>/', views.edit_book, name='book-edit'),
    path('delete_book/<int:pk>/', views.delete_book, name='book-delete'),


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
    path(
        'admin/', views.admin_view, name='admin_view'
    ),
    path(
        'librarian/', views.librarian_view, name='librarian_view'
    ),
    path(
        'member/', views.member_view, name='member_view'
    ),
    path('books/', views.list_books, name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),


]