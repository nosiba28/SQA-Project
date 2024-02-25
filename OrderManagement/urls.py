from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('payment/<int:id>/<int:id2>/',views.payment,name='payment'),
    path('<int:id>/',views.order,name='order'),
    path('receipt/<int:id>/',views.receipt,name='receipt')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
