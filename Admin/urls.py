from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('<int:id>/',views.aadmin,name='aadmin'),
    path('addProduct/<int:id>/',views.addProduct,name='addProduct'),
    path('updateProduct/<int:id>/',views.updateProduct,name='updateProduct'),
    path('removeProduct/<int:id>/',views.removeProduct,name='removeProduct'),
    path('allProduct/<int:id>/',views.allProduct,name='allProduct'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)