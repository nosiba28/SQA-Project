from django.test import TestCase, Client
from django.urls import reverse
from .models import Order, Customer, indOrder

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a sample order and customer for testing
        self.order = Order.objects.create(orderId=1, status=0)
        self.customer = Customer.objects.create(email="test@example.com", name="Test User")

        # Create sample ordered products for the order
        indOrder.objects.create(order=self.order, product_name="Product 1", quantity=2, price=10)
        indOrder.objects.create(order=self.order, product_name="Product 2", quantity=1, price=15)

        # Create a test client
        self.client = Client()

    def test_order_view(self):
        url = reverse('order', args=[self.order.orderId])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order.html')

    def test_payment_view(self):
        url = reverse('payment', args=[self.order.orderId, 1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment.html')

    def test_receipt_view(self):
        url = reverse('receipt', args=[self.order.orderId])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipt.html')

    def test_order_post(self):
        url = reverse('order', args=[self.order.orderId])
        response = self.client.post(url, {'pay': '1'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_payment_post(self):
        url = reverse('payment', args=[self.order.orderId, 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_receipt_post_confirm(self):
        url = reverse('receipt', args=[self.order.orderId])
        response = self.client.post(url, {'confirm': ''})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_receipt_post_back(self):
        url = reverse('receipt', args=[self.order.orderId])
        response = self.client.post(url, {'back': ''})
        self.assertEqual(response.status_code, 302)  # Redirect status code
