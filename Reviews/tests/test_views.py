import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from Reviews.models import Product, Review, Customer
from Search.models import Customer
from django.db import models
from Admin.models import Product

@pytest.mark.django_db
def test_review_view(client):
    """
    Test the review view to ensure it displays reviews correctly.

    This test checks if the review view returns a successful response
    and if the product and reviews are correctly included in the context.
    """
    # Create a test user
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
    # Create a test product
    product = Product.objects.create(productId=1, name='Test Product', price=10.00)
    # Create a test customer
    customer = Customer.objects.create(email='test@example.com', name='Test Customer')
    # Log the user in
    client.login(username='testuser', password='password')
    
    url = reverse('review', kwargs={'id': product.productId})
    response = client.get(url)
    assert response.status_code == 200
    # Ensure that the product is in the context
    assert 'product' in response.context
    assert response.context['product'] == product
    # Ensure that reviews are in the context
    assert 'reviews' in response.context
    assert list(response.context['reviews']) == list(Review.objects.filter(product=product))

@pytest.mark.django_db
def test_add_review(client):
    """
    Test adding a review via the review view.

    This test checks if a review can be successfully added through a POST request
    and if the review is stored correctly in the database.
    """
    # Create a test user
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
    # Create a test product
    product = Product.objects.create(productId=1, name='Test Product', price=10.00)
    # Create a test customer
    customer = Customer.objects.create(email='test@example.com', name='Test Customer')
    # Log the user in
    client.login(username='testuser', password='password')
    
    url = reverse('review', kwargs={'id': product.productId})
    response = client.post(url, {'comment': 'Test Comment', 'rating': 5, 'add': ''})
    assert response.status_code == 302  # Expecting a redirect after adding review
    # Check if review was added
    assert Review.objects.filter(product=product, customer=customer, comment='Test Comment').exists()
