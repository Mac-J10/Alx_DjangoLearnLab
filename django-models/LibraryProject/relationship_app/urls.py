from django.urls import path
from .views import LibraryDetailView

urlpatterns = [
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

app_name = 'relationship_app'
