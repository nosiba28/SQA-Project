from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views  # Importing views from the current directory
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

# URL patterns for the Order app
urlpatterns = [
    # URL pattern for handling payments with dynamic order and payment IDs
    path('payment/<int:id>/<int:id2>/', views.payment, name='payment'),

    # URL pattern for handling orders with dynamic order ID
    path('<int:id>/', views.order, name='order'),

    # URL pattern for handling receipts with dynamic order ID
    path('receipt/<int:id>/', views.receipt, name='receipt')
]

# Adding URL patterns for serving static files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Adding URL patterns for serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
