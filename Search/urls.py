from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',views.home,name='home'),
    path('logOut/',views.logOut,name='logOut'),
    path('logIn/',views.logIn,name='logIn'),
    path('register/',views.register,name='register'),
    path('product/',views.product,name='product')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)