from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from Wishlist.models import Wishlist
from Search.models import Customer
from Admin.models import Product
from Cart.models import Order, indOrder
from Wishlist.views import wishlist
from django.core.files.uploadedfile import SimpleUploadedFile

class WishlistViewTestCase(TestCase):
    """
    Test case for the Wishlist views.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.customer = Customer.objects.create(customerId=1, name='Test Customer', email='test@example.com', username='testuser', password='password')

        # Create a sample image file
        imageFile = open('F:\\Pictures\\Screenshots\\research.png', 'rb')
        imageData = imageFile.read()
        imageFile.close()

        # Create a product with an image
        self.productImage = SimpleUploadedFile("testImage.jpg", imageData, content_type="image/jpeg")
        self.product = Product.objects.create(productId=1, name='Test Product', price=10, image=self.productImage)

        self.order = Order.objects.create(customer=self.customer, orderId=1, status=0, total=0)
        self.wishlist = Wishlist.objects.create(customer=self.customer, product=self.product)

    def testWishlistView(self):
        """
        Test the Wishlist view.
        """
        # Create a request object
        request = self.factory.get('/wishlist/')
        request.user = self.user

        # Set up session data if needed
        request.session = {}

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = wishlist(request)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

    def testRemoveFromWishlist(self):
        """
        Test removing an item from the Wishlist.
        """
        # Create a request object
        request = self.factory.post('/wishlist/', {'remove': self.product.productId})
        request.user = self.user

        # Set up session data if needed
        request.session = {}

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = wishlist(request)

        # Check if the product is removed from the wishlist
        self.assertEqual(Wishlist.objects.filter(customer=self.customer, product=self.product).exists(), False)

    def testAddToCart(self):
        """
        Test adding an item from the Wishlist to the Cart.
        """
        # Create a request object
        request = self.factory.post('/wishlist/', {'addcart': self.product.productId})
        request.user = self.user

        # Set up session data if needed
        request.session = {}

        # Attach the user to the request
        request.user = self.user

        # Attach the request to the view and get the response
        response = wishlist(request)

        # Check if the product is added to the cart
        self.assertEqual(indOrder.objects.filter(order=self.order, product=self.product).exists(), True)