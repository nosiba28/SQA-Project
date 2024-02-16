from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

# Define URL patterns for the admin app
urlpatterns = [
    # Path for accessing the aadmin view with shop ID as parameter
    path('<int:id>/', views.aadmin, name='aadmin'),
    # Path for adding a product with shop ID as parameter
    path('addProduct/<int:id>/', views.addProduct, name='addProduct'),
    # Path for updating a product with product ID as parameter
    path('updateProduct/<int:id>/', views.updateProduct, name='updateProduct'),
    # Path for removing a product with product ID as parameter
    path('removeProduct/<int:id>/', views.removeProduct, name='removeProduct'),
    # Path for viewing all products with shop ID as parameter
    path('allProduct/<int:id>/', views.allProduct, name='allProduct'),
]

# Add URL patterns for serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Add URL patterns for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
