from django.test import TestCase, Client
from django.urls import reverse
from Search.models import Owner, Customer
from Admin.models import Product
from Refund.models import RefundRequest
from Cart.models import indOrder, Order 

from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class RefundViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Creating a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

        # Creating sample data for testing
        self.product = Product.objects.create(productId=1, name='Test Product', desc='Test Description', price=10)
        self.order = Order.objects.create(orderId=1, status=1)
        self.ind_order = indOrder.objects.create(order=self.order, product=self.product)

    def test_refund_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('refund'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'refund.html')

    def test_refund_view_post(self):
        self.client.login(username='testuser', password='password')
        data = {
            'order': self.order.orderId,
            'apply': self.product.productId,
            'reason': 'Test Reason'
        }
        response = self.client.post(reverse('refund'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after POST
        self.assertEqual(response.url, '/refund')  # Redirects back to the refund page

        # Check if refund request has been created
        refund_request = RefundRequest.objects.filter(order=self.order, product=self.product).first()
        self.assertIsNotNone(refund_request)
        self.assertEqual(refund_request.reason, 'Test Reason')

    def test_manage_refund_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('manageRefund'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manageRefund.html')

    def test_manage_refund_view_post_accept(self):
        self.client.login(username='testuser', password='password')
        data = {
            'order': self.order.orderId,
            'product': self.product.productId,
            'accept': True
        }
        response = self.client.post(reverse('manageRefund'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after POST
        self.assertEqual(response.url, '/refund/manage')  # Redirects back to the manage refund page

        # Check if refund request status and indOrder status have been updated
        refund_request = RefundRequest.objects.filter(order=self.order, product=self.product).first()
        self.assertIsNotNone(refund_request)
        self.assertEqual(refund_request.status, 1)
        self.assertEqual(self.ind_order.status, 2)

    def test_manage_refund_view_post_reject(self):
        self.client.login(username='testuser', password='password')
        data = {
            'order': self.order.orderId,
            'product': self.product.productId,
            'reject': True
        }
        response = self.client.post(reverse('manageRefund'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after POST
        self.assertEqual(response.url, '/refund/manage')  # Redirects back to the manage refund page

        # Check if refund request status and indOrder status have been updated
        refund_request = RefundRequest.objects.filter(order=self.order, product=self.product).first()
        self.assertIsNotNone(refund_request)
        self.assertEqual(refund_request.status, 1)
        self.assertEqual(self.ind_order.status, 3)
