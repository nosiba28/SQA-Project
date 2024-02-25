from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Search.urls')),
    path('cart/',include('Cart.urls')),
    path('aadmin/',include('Admin.urls')),
    path('order/',include('OrderManagement.urls')),
    path('wishlist/',include('Wishlist.urls')),
    path('review/',include('Reviews.urls')),
    path('dashboard/',include('Dashboard.urls')),
    path('offer/',include('Offer.urls')), 
    path('refund/',include('Refund.urls')),

]
