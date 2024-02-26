from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Path for viewing and adding reviews for a product
    # The URL pattern expects an integer ID parameter which represents the product's ID
    # When accessed, this URL triggers the 'review' view function in the 'views.py' file
    # The name 'review' is assigned to this URL pattern, which can be used to reverse it in Django templates
    path('<int:id>/', views.review, name='review'),
]

# Serving static files during development
# Static files include CSS, JavaScript, images, etc.
# These settings are used to serve static files uploaded by users or required by the application itself
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files during development
# Media files include user-uploaded files like images, videos, etc.
# These settings are used to serve media files uploaded by users
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
