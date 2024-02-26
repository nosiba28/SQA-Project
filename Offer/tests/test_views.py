import pytest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
# from .models import *

# from .models import Owner, Product, Category
from Search.models import Customer, Owner
from Admin.models import Product, Category
from django.contrib.auth.models import User
from Offer.views import offer
# In Offer/tests/test_views.py

# Create your tests here.

class OfferViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='nsb_01', email='nsb@gmail.com', password='nsb12345')
        self.owner = Owner.objects.create(email='nsb@gmail.com')
        self.category = Category.objects.create(categoryName='Shoe')
        self.product = Product.objects.create(productId=1,name='shoe33', price=1406, shop=self.owner, category=self.category)

    def test_offer_view(self):
        # Create a request object
        request = self.factory.get('/offer/')
        request.user = self.user

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = offer(request)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Create a request object
        request = self.factory.get('/offer/')
        request.user = self.user

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = offer(request)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)


    def test_apply_offer_to_categories(self):
        request = self.factory.post('/offer/', {'apply': '', 'category': [self.category.categoryName], 'disc': 10})
        request.user = self.user

        response = offer(request)
        self.assertEqual(response.status_code, 302)  # Redirects after applying offer

        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.offer, 10)  # Check if the offer is applied correctly

    def test_apply_offer_to_all_products(self):
        request = self.factory.post('/offer/', {'all': '', 'disc': 10})
        request.user = self.user

        response = offer(request)
        self.assertEqual(response.status_code, 302)  # Redirects after applying offer

        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.offer, 10)  # Check if the offer is applied correctly
    
    def test_discard_offer(self):
        # Set an offer first
        self.product.offer = 10
        self.product.save()

        request = self.factory.post('/offer/', {'discard': ''})
        request.user = self.user

        response = offer(request)
        self.assertEqual(response.status_code, 302)  # Redirects after discarding offer

        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.offer, 0)  # Check if the offer is discarded correctly

    def test_apply_individual_offer(self):
        
        # Create a request object with POST data
        request = self.factory.post('/offer/', {'ind': '', 'ind': self.product.pk, 'discount': 10})
     
        request.user = self.user

        # Attach the request to the view and get the response
        response = offer(request)

        # Check if the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Reload the product from the database
        updated_product = Product.objects.get(pk=self.product.pk)

        # Check if the individual offer is applied correctly
        self.assertEqual(updated_product.offer, 10)

   