from django.test import TestCase, Client
from django.urls import reverse
from .models import Owner, Customer

# Create your tests here.
class ViewTestCase(TestCase):
    def setUp(self):
        # Create some sample users for testing
        self.owner = Owner.objects.create(
            name='Test Owner',
            shopName='Test Shop',
            shopId=1,
            username='test_owner',
            email='testowner@example.com',
            password='testpassword'
        )
        self.customer = Customer.objects.create(
            customerId=1,
            name='Test Customer',
            username='test_customer',
            email='testcustomer@example.com',
            password='testpassword'
        )

    def test_home_view(self):
        # Test home page view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Check if the home page returns a 200 status code

    def test_login_view(self):
        # Test login view with valid credentials
        response = self.client.post(reverse('logIn'), {'email': 'testowner@example.com', 'password': 'testpassword', 'type': '2'})
        self.assertEqual(response.status_code, 302)  # Check if the login redirects after successful login

    def test_register_view(self):
        # Test register view
        response = self.client.post(reverse('register'), {'type': '2', 'name': 'New Owner', 'shop': 'New Shop', 'username': 'new_owner', 'email': 'newowner@example.com', 'pass': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # Check if the registration redirects after successful registration

    def test_logout_view(self):
        # Test logout view
        response = self.client.get(reverse('logOut'))
        self.assertEqual(response.status_code, 302)  # Check if the logout redirects after successful logout
