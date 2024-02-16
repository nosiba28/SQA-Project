# # tests.py

# from django.test import TestCase, RequestFactory
# from django.contrib.auth.models import User
# from .models import Category, Product
# from Search.models import Owner
# from .views import aadmin, allProduct, addProduct, updateProduct, removeProduct

# # UNIT TESTING STARTS HERE

# # unit tests for the models

# class CategoryModelTest(TestCase):
#     def test_category_str(self):
#         category = Category.objects.create(categoryName="Test Category")
#         self.assertEqual(str(category), "Test Category")

# class ProductModelTest(TestCase):
#     def test_product_str(self):
#         product = Product.objects.create(
#             productId=1,
#             name="Test Product",
#             desc="Test Description",
#             price=10
#         )
#         self.assertEqual(str(product), "1 - Test Product")


# # unit tests for the views

# class AdminViewsTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='testuser', password='12345')

#     def test_aadmin_view(self):
#         request = self.factory.get('/aadmin/1/')
#         request.user = self.user
#         response = aadmin(request, id=1)
#         self.assertEqual(response.status_code, 200)

#     def test_allProduct_view(self):
#         category = Category.objects.create(categoryName="Test Category")
#         shop = Owner.objects.create(shopId=1)
#         product = Product.objects.create(
#             productId=1,
#             name="Test Product",
#             desc="Test Description",
#             price=10,
#             category=category,
#             shop=shop
#         )
#         request = self.factory.get('/aadmin/allProduct/1/')
#         request.user = self.user
#         response = allProduct(request, id=1)
#         self.assertEqual(response.status_code, 200)

#     def test_addProduct_view(self):
#         request = self.factory.get('/aadmin/addProduct/1/')
#         request.user = self.user
#         response = addProduct(request, id=1)
#         self.assertEqual(response.status_code, 200)

#     def test_updateProduct_view(self):
#         request = self.factory.get('/aadmin/updateProduct/1/')
#         request.user = self.user
#         response = updateProduct(request, id=1)
#         self.assertEqual(response.status_code, 200)

#     def test_removeProduct_view(self):
#         request = self.factory.get('/aadmin/removeProduct/1/')
#         request.user = self.user
#         response = removeProduct(request, id=1)
#         self.assertEqual(response.status_code, 200)


from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(categoryName='Electronics')

    def test_category_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.categoryName
        self.assertEqual(expected_object_name, 'Electronics')

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(productId=1, name='Laptop', desc='High performance laptop', price=1000)

    def test_product_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = product.name
        self.assertEqual(expected_object_name, 'Laptop')

    def test_product_str_representation(self):
        product = Product.objects.get(id=1)
        expected_str = f"{product.productId} - None"  # Assuming shop ID is not defined
        self.assertEqual(str(product), expected_str)

    def test_product_default_values(self):
        product = Product.objects.get(id=1)
        self.assertIsNone(product.image)  # Image should be None by default

    def test_product_null_values(self):
        product = Product.objects.get(id=1)
        self.assertIsNone(product.desc)  # Desc can be null
