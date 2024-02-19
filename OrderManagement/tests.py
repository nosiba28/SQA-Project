from django.test import TestCase, Client
from django.urls import reverse
from .models import Order, Customer
from django.contrib.auth.models import User

class OrderViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()  # Initialize the test client
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a customer
        self.customer = Customer.objects.create(
            customerId=1,
            name="Test Customer",
            email="test@example.com",
            username="testuser",
            password="testpassword"
        )
        # Create an order
        self.order = Order.objects.create(
            orderId=1,
            customer=self.customer,
            total=100
        )

    def test_order_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Make a GET request to the order view
        response = self.client.get(reverse('order', args=[self.order.id]))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered template is correct
        self.assertTemplateUsed(response, 'order.html')

    def test_payment_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Make a GET request to the payment view
        response = self.client.get(reverse('payment', args=[self.order.id, 1]))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered template is correct
        self.assertTemplateUsed(response, 'payment.html')

  