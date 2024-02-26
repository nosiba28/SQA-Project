from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

"""
    URL patterns for the application.

    URL Configuration Commands:
    - Directs requests to the 'offer' view.

    Parameters:
        path (str): The URL path to match.
        views.offer (function): The view function to be called.
        name (str): The name used to identify the URL pattern.

    Returns:
        list: List of URL patterns.
"""

urlpatterns = [
    path('',views.offer,name='offer'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)