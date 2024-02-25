from django.db import models
from Search.models import Customer
from Admin.models import Product

class Wishlist(models.Model):
    """
    Represents a Wishlist item.

    Each Wishlist item is associated with a specific product and customer.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    """
    The product associated with this Wishlist item.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    """
    The customer who added this product to the Wishlist.
    """

    def __str__(self):
        """
        Returns a string representation of the Wishlist item.

        Returns:
            str: A string representing the Wishlist item, in the format 'ProductID - CustomerID'.
        """
        return str(self.product.productId) + " - " + str(self.customer.customerId)
