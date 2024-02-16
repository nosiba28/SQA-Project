from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the current directory

# Define URL patterns
urlpatterns = [
    # URL pattern for handling payment with dynamic order id and payment method id
    path('payment/<int:id>/<int:id2>/', views.payment, name='payment'),

    # URL pattern for handling orders with dynamic order id
    path('<int:id>/', views.order, name='order'),

    # URL pattern for handling receipts with dynamic order id
    path('receipt/<int:id>/', views.receipt, name='receipt')
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
