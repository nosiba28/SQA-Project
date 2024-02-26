from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from Wishlist.models import Wishlist
from Search.models import Customer
from Admin.models import Product
from Cart.models import Order, indOrder
from Wishlist.views import wishlist
from django.core.files.uploadedfile import SimpleUploadedFile

