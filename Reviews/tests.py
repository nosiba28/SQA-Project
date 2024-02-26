from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Review, Customer

class ReviewViewTest(TestCase):
    """
    Test cases for the review view.

    These test cases ensure that the review view functions correctly,
    including displaying reviews for a product and adding new reviews.
    """

    def setUp(self):
        """
        Set up test data before each test case.

        This method creates necessary test objects such as a test user,
        a test product, and a test customer, and logs the user in.
        """
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        # Create a test product
        self.product = Product.objects.create(productId=1, name='Test Product', price=10.00)
        # Create a test customer
        self.customer = Customer.objects.create(email='test@example.com', name='Test Customer')
        # Log the user in
        self.client.login(username='testuser', password='password')

    def test_review_view(self):
        """
        Test the review view to ensure it displays reviews correctly.

        This test checks if the review view returns a successful response
        and if the product and reviews are correctly included in the context.
        """
        url = reverse('review', kwargs={'id': self.product.productId})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Ensure that the product is in the context
        self.assertIn('product', response.context)
        self.assertEqual(response.context['product'], self.product)
        # Ensure that reviews are in the context
        self.assertIn('reviews', response.context)
        self.assertEqual(list(response.context['reviews']), list(Review.objects.filter(product=self.product)))

    def test_add_review(self):
        """
        Test adding a review via the review view.

        This test checks if a review can be successfully added through a POST request
        and if the review is stored correctly in the database.
        """
        url = reverse('review', kwargs={'id': self.product.productId})
        response = self.client.post(url, {'comment': 'Test Comment', 'rating': 5, 'add': ''})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after adding review
        # Check if review was added
        self.assertTrue(Review.objects.filter(product=self.product, customer=self.customer, comment='Test Comment').exists())

    def tearDown(self):
        """
        Clean up after each test case.

        This method deletes the test user, test product, and test customer
        to ensure a clean state for subsequent test cases.
        """
        # Clean up
        self.user.delete()
        self.product.delete()
        self.customer.delete()
