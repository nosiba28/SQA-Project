from django.db import models

# Creating Category model
class Category(models.Model):
    """
    Model for product category
    """

    # Define categoryName field for Category model
    categoryName = models.CharField(max_length=100, blank=True, null=True)

    # Return string representation of the Category object
    def __str__(self):
        return str(self.categoryName) 

# Creating Product model
class Product(models.Model):
    """
    Model for product
    """

    # Define productId field for Product model
    productId = models.IntegerField(default=0, blank=True, null=True)
    # Define name field for Product model
    name = models.CharField(max_length=40, blank=True, null=True)
    # Define image field for Product model
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    # Define desc field for Product model
    desc = models.CharField(max_length=100, blank=True, null=True, default=None)
    # Define price field for Product model
    price = models.IntegerField(default=0, blank=True, null=True)

    # Return string representation of the Product object
    def __str__(self):
        return str(self.productId) + " - " + str(self.shop.shopId)
