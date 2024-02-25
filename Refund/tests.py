# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from .models import *
# from Dashboard.models import *
# from Search.models import *
# from Cart.models import *
# from Wishlist.models import *
# from Admin.models import *

# # Create your tests here

# class RefundTestCase(TestCase):
#     """
#         This class tests the refund feature, including viewing the refund page and submitting a refund request
#     """

#     def setUp(self):
#         """
#         Set up test data.

#         This method sets up the necessary test data before running each test case.
#         """
#         self.client = Client()
#         self.user1 = User.objects.create_user(username='testuser1', email='test1@example.com', password='password1')
#         self.user2 = User.objects.create_user(username='testuser2', email='test2@example.com', password='password2')
#         self.customer = Customer.objects.create(name="test_buyer",username='testuser1', email='test1@example.com', password='password1')
#         self.owner = Owner.objects.create(name="test_owner",username='testuser2', email='test2@example.com', password='password2')

#         self.product = Product.objects.create(productId=1, name='Test Product', price=10,offerPrice=10, shop=self.owner)
#         self.orderObject1=Order.objects.create(customer=self.customer,orderId=1,status=1)
#         self.orderObject2=Order.objects.create(customer=self.customer,orderId=2,status=1)
#         self.order1 = indOrder.objects.create(date='2024-02-22', product=self.product, quantity=2, order=self.orderObject1)
#         self.order2 = indOrder.objects.create(date='2024-02-24', product=self.product, quantity=1, order=self.orderObject2)

    
#     def test_refund_view(self):
#         """
#         Test viewing the refund page

#         This method tests whether the refund page can be accessed successfully.
#         """
#         self.client.force_login(self.user1)
#         response = self.client.get(reverse('refund'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'refund.html')

    
#     def test_refund_request(self):
#         """
#         Test submitting a refund request

#         This method tests whether a refund request can be successfully submitted.
#         """
#         self.client.force_login(self.user1)
#         data = {
#         'reason': 'Defective product',
#         'order': self.order1.order.id,  # Extract the order ID from the order instance
#         'apply': self.product.id
#         }
#         response = self.client.post(reverse('refund'), data)
#         self.assertEqual(response.status_code, 302)

#         # Redirect after form submission    

"""
    def test_manage_refund_view(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse('manage_refund'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manageRefund.html')

    def test_refund_request(self):
        self.client.force_login(self.user1)
        data = {
            'reason': 'Defective product',
            'order': self.order1,
            'apply': self.product
        }
        response = self.client.post(reverse('refund'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission

    def test_manage_refund_accept(self):
        refund_request = RefundRequest.objects.create(reason='Defective product', order=self.order, product=self.product)
        self.client.force_login(self.owner)
        data = {
            'order': self.order1,
            'product': self.product,
            'accept': True
        }
        response = self.client.post(reverse('manage_refund'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        refund_request.refresh_from_db()
        self.assertEqual(refund_request.status, 1)
        self.assertEqual(self.ind_order.status, 2)  # Check if indOrder status is updated

    def test_manage_refund_reject(self):
        refund_request = RefundRequest.objects.create(reason='Defective product', order=self.order, product=self.product)
        self.client.force_login(self.owner)
        data = {
            'order': self.order.id,
            'product': self.product.id,
            'reject': True
        }
        response = self.client.post(reverse('manage_refund'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        refund_request.refresh_from_db()
        self.assertEqual(refund_request.status, 1)
        self.assertEqual(self.ind_order.status, 3)  # Check if indOrder status is updated
"""

# Assuming 'refund' and 'manage_refund' are the names of the views registered in the urls.py file.
