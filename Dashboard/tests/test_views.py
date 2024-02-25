# Dashboard/tests.py
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from Dashboard.views import dashboard
from datetime import datetime
from django.urls import reverse
from Dashboard.models import *
from Search.models import *
from Cart.models import *
from Wishlist.models import *
from Admin.models import *
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

# Create your tests here

class DashboardViewLoginTest(TestCase):
    def setUp(self):
        # Create test data (admin user)
        self.user1 = User.objects.create_user(username='test_admin', email='test_admin@example.com', password='testpassword')
        self.user2 = User.objects.create_user(username='test_customer', email='test_customer@example.com', password='testpassword')
        self.admin = Owner.objects.create(shopId=1, name='Test Shop', email=self.user1.email, shopName='Test Shop', password='testpassword', username='test_admin')
        self.customer = Customer.objects.create(name="test_buyer",username='test_customer', email='test_customer@example.com', password='testpassword')


    def test_login_and_access(self):
        # Log in the admin
        self.client.login(username='test_admin', password='testpassword')

        # Make a GET request to the dashboard view
        response = self.client.get(reverse('dashboard'))

        # Assert successful response and access to the view
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')



class DashboardViewOrdersTest(TestCase):
    def setUp(self):
        # Create test data (admin and orders)
        self.user1 = User.objects.create_user(username='test_admin', email='test_admin@example.com', password='testpassword')
        self.admin = Owner.objects.create(shopId=1, name='Test Shop', email=self.user1.email, shopName='Test Shop', password='testpassword', username='test_admin')

        self.user2 = User.objects.create_user(username='test_customer', email='test_customer@example.com', password='testpassword')
        self.customer = Customer.objects.create(name="test_buyer",username='test_customer', email='test_customer@example.com', password='testpassword')
    
        self.product = Product.objects.create(productId=1, name='Test Product', price=10,offerPrice=10, shop=self.admin)
        self.orderObject1=Order.objects.create(customer=self.customer,orderId=1,status=1)
        self.orderObject2=Order.objects.create(customer=self.customer,orderId=2,status=1)
        self.order1 = indOrder.objects.create(date='2024-02-22', product=self.product, quantity=2, order=self.orderObject1)
        self.order2 = indOrder.objects.create(date='2024-02-24', product=self.product, quantity=1, order=self.orderObject2)

    def testOrdersRendering(self):
        # Log in the admin
        self.client.login(username='test_admin', password='testpassword')

        # Make a GET request to the dashboard view
        response = self.client.get(reverse('dashboard'))

        # Assert that orders context variable contains expected data
        self.assertEqual(response.context['orders'].count(), 2)
        self.assertIn(self.order1, response.context['orders'])
        self.assertIn(self.order2, response.context['orders'])



class DashboardViewChartsTest(TestCase):
    def setUp(self):
        # Create test data (admin and orders)
        self.user1 = User.objects.create_user(username='test_admin', email='test_admin@example.com', password='testpassword')
        self.admin = Owner.objects.create(shopId=1, name='Test Shop', email=self.user1.email, shopName='Test Shop', password='testpassword', username='test_admin')
        self.product1 = Product.objects.create(productId=1, name='Test Product 1', price=10,offerPrice=10, shop=self.admin)
        self.product2 = Product.objects.create(productId=2, name='Test Product 2', price=20,offerPrice=20, shop=self.admin)
        self.user2 = User.objects.create_user(username='test_customer', email='test_customer@example.com', password='testpassword')
        self.customer = Customer.objects.create(name="test_buyer",username='test_customer', email='test_customer@example.com', password='testpassword')
        self.orderObject1=Order.objects.create(customer=self.customer,orderId=1,status=1)
        self.orderObject2=Order.objects.create(customer=self.customer,orderId=2,status=1)
        self.orderObject3=Order.objects.create(customer=self.customer,orderId=3,status=1)
        self.order1 = indOrder.objects.create(date='2024-02-22', product=self.product1, quantity=2, order=self.orderObject1)
        self.order2 = indOrder.objects.create(date='2024-02-23', product=self.product2, quantity=1, order=self.orderObject2)
        self.order3 = indOrder.objects.create(date='2024-02-24', product=self.product1, quantity=3, order=self.orderObject3)

    def testLineChartData(self):
        # Log in the admin
        self.client.login(username='test_admin', password='testpassword')

        # Make a GET request to the dashboard view
        response = self.client.get(reverse('dashboard'))

        # Assert expected line chart data
        expected_labels = ['2024-02-22', '2024-02-23', '2024-02-24']
        expected_data = [20, 20, 30]
          # 2 * 10 + 1 * 20 + 3 * 10
        print(response.context['lineLabels'])

        self.assertEqual(response.context['lineLabels'], expected_labels)
        self.assertEqual(response.context['lineData'], expected_data)

        # Same as line chart test, but for pie chart data
        expected_labels = ['Test Product 1', 'Test Product 2']
        expected_data = [5, 1]  # 2 + 3 + 1
        self.assertEqual(response.context['pieLabels'], expected_labels)
        self.assertEqual(response.context['pieData'], expected_data)

        # Assert expected month chart data
        expected_labels = ['2024-February']
        expected_data = [70]  # 2 * 10 + 20 + 3 * 10
        self.assertEqual(response.context['monthLabels'], expected_labels)
        self.assertEqual(response.context['monthData'], expected_data)

    def testEmptyDataHandling(self):
        # Create an empty order list
        indOrder.objects.all().delete()

        # Login and make a request
        self.client.login(username='test_admin', password='testpassword')
        response = self.client.get(reverse('dashboard'))

        # Assert empty data in context
        self.assertEqual(response.context['orders'].count(), 0)
        self.assertEqual(len(response.context['lineLabels']), 0)
        self.assertEqual(len(response.context['lineData']), 0)
        self.assertEqual(len(response.context['pieLabels']), 0)
        self.assertEqual(len(response.context['pieData']), 0)
        self.assertEqual(len(response.context['monthLabels']), 0)
        self.assertEqual(len(response.context['monthData']), 0)



