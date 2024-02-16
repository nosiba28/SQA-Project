# tests.py

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Category, Product
from .views import aadmin, allProduct, addProduct, updateProduct, removeProduct

# UNIT TESTING STARTS HERE

# unit tests for the models

class CategoryModelTest(TestCase):
    def test_category_str(self):
        category = Category.objects.create(categoryName="Test Category")
        self.assertEqual(str(category), "Test Category")

class ProductModelTest(TestCase):
    def test_product_str(self):
        product = Product.objects.create(
            productId=1,
            name="Test Product",
            desc="Test Description",
            price=10
        )
        self.assertEqual(str(product), "1 - Test Product")


# unit tests for the views

class AdminViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_aadmin_view(self):
        request = self.factory.get('/aadmin/1/')
        request.user = self.user
        response = aadmin(request, id=1)
        self.assertEqual(response.status_code, 200)

    def test_allProduct_view(self):
        category = Category.objects.create(categoryName="Test Category")
        shop = Owner.objects.create(shopId=1)
        product = Product.objects.create(
            productId=1,
            name="Test Product",
            desc="Test Description",
            price=10,
            category=category,
            shop=shop
        )
        request = self.factory.get('/aadmin/allProduct/1/')
        request.user = self.user
        response = allProduct(request, id=1)
        self.assertEqual(response.status_code, 200)

    def test_addProduct_view(self):
        request = self.factory.get('/aadmin/addProduct/1/')
        request.user = self.user
        response = addProduct(request, id=1)
        self.assertEqual(response.status_code, 200)

    def test_updateProduct_view(self):
        request = self.factory.get('/aadmin/updateProduct/1/')
        request.user = self.user
        response = updateProduct(request, id=1)
        self.assertEqual(response.status_code, 200)

    def test_removeProduct_view(self):
        request = self.factory.get('/aadmin/removeProduct/1/')
        request.user = self.user
        response = removeProduct(request, id=1)
        self.assertEqual(response.status_code, 200)
