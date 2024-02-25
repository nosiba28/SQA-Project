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



# Test for view:


class CartViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='ema_01', email='ema@gmail.com', password='ema12345')
        self.customer = Customer.objects.create(customerId=101, name='ema', email='ema@gmail.com', username='ema_01', password='ema12345')
        self.order = Order.objects.create(customer=self.customer, orderId=1, status=0, total=0)
        self.product = Product.objects.create(productId=102, name='Shirt', price=100)

    def testCartView(self):
        # Create a request object
        request = self.factory.get('/cart/')
        request.user = self.user

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = cart(request)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

    def testCartPostOrder(self):
        # Create a request object with POST data
        request = self.factory.post('/cart/', {'order': ''})
        request.user = self.user

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = cart(request)

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

    def testCartPostUpdateQuantity(self):
        # Create a request object with POST data
        request = self.factory.post('/cart/', {'product': [self.product.productId]})
        request.user = self.user

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = cart(request)

        # Check if the response is a redirect (status code 302)
        if response.status_code == 302:
         print("Redirect URL:", response.url)

        # Assert the status code of the response
        self.assertEqual(response.status_code, 200)
