from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

"""
    URL patterns for the application.

    These patterns map URLs to views within the application.

    Attributes:
        cart (view): The view function handling requests to the cart page.

    URL Patterns:
        '' (str): The root URL, mapped to the cart view.
"""

urlpatterns = [
    path('',views.cart,name='cart'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
