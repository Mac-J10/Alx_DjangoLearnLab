from django.urls import path, include

urlpatterns = [
    # … other routes …
    path('relationship/', include('relationship_app.urls')),
]