from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views  # Importing views module from the current directory
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

# Define URL patterns for the application
urlpatterns = [
    # Path to access the review view with an integer parameter 'id'
    path('<int:id>/', views.review, name='review'),
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
