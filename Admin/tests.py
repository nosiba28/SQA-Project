from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Product

# Unit test cases for Admin models

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(categoryName='Electronics')

    def test_product_creation(self):
        category = Category.objects.get(id=1)
        
        # Create a simple image file (a 1x1 pixel white image)
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        product = Product.objects.create(
            productId=1,
            name='Laptop',
            desc='High performance laptop',
            price=1000,
            image=image_file,  # Provide the image file
            shop='ABC Shop'  # Example local field value
        )

        # Retrieve the created product from the database
        saved_product = Product.objects.get(id=1)

        # Check if the product attributes match the provided values
        self.assertEqual(saved_product.productId, 1)
        self.assertEqual(saved_product.name, 'Laptop')
        self.assertEqual(saved_product.desc, 'High performance laptop')
        self.assertEqual(saved_product.price, 1000)
        # Check if the image file is stored (expecting an auto-generated name)
        self.assertTrue(saved_product.image.name.startswith('image/test_image_'))  
        self.assertEqual(saved_product.shop, 'ABC Shop')

    def test_product_str_representation(self):
        category = Category.objects.get(id=1)
        product = Product.objects.create(
            productId=1,
            name='Laptop',
            desc='High performance laptop',
            price=1000,
            shop='ABC Shop'  
        )

        expected_str = '1 - ABC Shop'  # Expected string representation
        self.assertEqual(str(product), expected_str)



# unit testing for views
