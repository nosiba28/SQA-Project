from django.test import TestCase, RequestFactory
from Cart.models import Order, indOrder
from Search.models import Customer
from Admin.models import Product
from django.contrib.auth.models import User
from .views import cart


# Create your tests here.

#Test for Model:

class TestModelOrder(TestCase):

    def setUp(self):
        # Here we try to create the instances for testing
        self.customer = Customer.objects.create(name='Ema', email='ema@gmail.com')
        self.order = Order.objects.create(customer=self.customer, orderId=1, status=1, total=100)

    def testOrderStr(self):
        # Test the __str__ method of the Order model
        self.assertEqual(str(self.order), '1')

class TestModelIndOrder(TestCase):
    def setUp(self):
        # We create the instances for testing
        self.customer = Customer.objects.create(name='Ema', email='ema@gmail.com')
        self.product = Product.objects.create(name='Shirt', price=2300)
        self.order = Order.objects.create(customer=self.customer, orderId=1, status=1, total=4500)
        self.ind_order = indOrder.objects.create(product=self.product, order=self.order, quantity=2)

    def testIndOrderStr(self):
        # Test the __str__ method of the indOrder model
        expected_str = f'{self.order.orderId} - {self.product.productId}'
        self.assertEqual(str(self.ind_order), expected_str)





