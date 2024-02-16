# from django.test import TestCase
# from django.core.files.uploadedfile import SimpleUploadedFile
# from .models import Category, Product

# # Unit test cases for Admin models

# class ProductModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Category.objects.create(categoryName='Electronics')

#     def test_product_creation(self):
#         category = Category.objects.get(id=1)
        
#         # Create a simple image file (a 1x1 pixel white image)
#         image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
#         product = Product.objects.create(
#             productId=1,
#             name='Laptop',
#             desc='High performance laptop',
#             price=1000,
#             image=image_file,  # Provide the image file
#             shop='ABC Shop'  # Example local field value
#         )

#         # Retrieve the created product from the database
#         saved_product = Product.objects.get(id=1)

#         # Check if the product attributes match the provided values
#         self.assertEqual(saved_product.productId, 1)
#         self.assertEqual(saved_product.name, 'Laptop')
#         self.assertEqual(saved_product.desc, 'High performance laptop')
#         self.assertEqual(saved_product.price, 1000)
#         # Check if the image file is stored (expecting an auto-generated name)
#         self.assertTrue(saved_product.image.name.startswith('image/test_image_'))  
#         self.assertEqual(saved_product.shop, 'ABC Shop')

#     def test_product_str_representation(self):
#         category = Category.objects.get(id=1)
#         product = Product.objects.create(
#             productId=1,
#             name='Laptop',
#             desc='High performance laptop',
#             price=1000,
#             shop='ABC Shop'  
#         )

#         expected_str = '1 - ABC Shop'  # Expected string representation
#         self.assertEqual(str(product), expected_str)

# from Search.models import Owner

# # unit testing for views


from .models import Product
from Search.models import Owner

from django.test import TestCase, Client
from django.urls import reverse
from .models import Product
from django.core.files.uploadedfile import SimpleUploadedFile

class ViewTestCase(TestCase):
    def setUp(self):
        # Create a sample owner for testing
        self.owner = Owner.objects.create(
            name='Test Owner',
            shopName='Test Shop',
            shopId=1,
            username='test_owner',
            email='testowner@example.com',
            password='testpassword'
        )

    def test_add_product_view(self):
        # Create a sample image file for testing
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        # Test add product view
        response = self.client.post(reverse('addProduct', args=[self.owner.shopId]), 
                                    {'name': 'New Product', 'desc': 'New Description', 'price': 20, 'image': image_file})
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after adding a product

    def test_update_product_view(self):
        # Create a sample product associated with the owner
        product = Product.objects.create(
            shop=self.owner,
            productId=1,
            name='Test Product',
            desc='Test Description',
            price=10
        )
        
        # Create a sample image file for testing
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        # Test update product view
        response = self.client.post(reverse('updateProduct', args=[self.owner.shopId]), 
                                    {'id': product.productId, 'name': 'Updated Product', 'desc': 'Updated Description', 'price': 15, 'image': image_file})
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after updating a product

    def test_remove_product_view(self):
        # Create a sample product associated with the owner
        product = Product.objects.create(
            shop=self.owner,
            productId=1,
            name='Test Product',
            desc='Test Description',
            price=10
        )
        
        # Test remove product view
        response = self.client.post(reverse('removeProduct', args=[self.owner.shopId]), {'id': product.productId})
        self.assertEqual(response.status_code, 302)  

    def test_all_product_view(self):
        # Test all product view
        response = self.client.get(reverse('allProduct', args=[self.owner.shopId]))
        self.assertEqual(response.status_code, 200)