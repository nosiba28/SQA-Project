from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from Refund.models import *
from Dashboard.models import *
from Search.models import *
from Cart.models import *
from Wishlist.models import *
from Admin.models import *
class ManageRefundViewTestCase(TestCase):
    """
    Test cases for the manageRefund view.
    """

    def setUp(self):
        """
        Set up test data.
        """
        # Create users
        self.user1 = User.objects.create_user(username='testuser1', email='test1@example.com', password='password1')
        self.user2 = User.objects.create_user(username='testuser2', email='test2@example.com', password='password2')

        # Create customer
        self.customer = Customer.objects.create(customerId=1, name="Test Buyer", email='test1@example.com', username='testuser1', password='password1')

        # Create owner
        self.owner = Owner.objects.create(shopId=1, name="Test Owner", email='test2@example.com', username='testuser2', password='password2')

        # Create product
        self.product = Product.objects.create(productId=1, name='Test Product', price=10, shop=self.owner)

        # Create order
        self.order = Order.objects.create(customer=self.customer, orderId=1, status=1)

        # Create individual order
        self.ind_order = indOrder.objects.create(date='2024-02-22', product=self.product, quantity=2, order=self.order, status=0)

        # Create refund request
        self.refund_request = RefundRequest.objects.create(reason='Defective product', product=self.product, order=self.order, status=0)

    def test_manage_refund_view_accessible(self):
        """
        Test whether the manage refund page is accessible.
        """
        client = Client()
        client.force_login(self.user2)
        response = client.get(reverse('manageRefund'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manageRefund.html')

    def test_refund_request_acceptance(self):
        """
        Test accepting a refund request.
        """
        client = Client()
        client.force_login(self.user2)
        data = {
            'order': self.order.id,
            'product': self.product.id,
            'accept': 'accept'
        }
        response = client.post(reverse('manageRefund'), data)
        self.assertEqual(response.status_code, 302)  # Here a successful acceptance redirects