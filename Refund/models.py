from django.db import models
from Admin.models import Product
from Cart.models import Order

class RefundRequest(models.Model):
    """
    Model representing a refund request.

    Attributes:
        reason (str): The reason for the refund request.
        product (Product): The product associated with the refund request.
        order (Order): The order associated with the refund request.
        status (int): The status of the refund request.
    """

    reason = models.CharField(max_length=100, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the refund request.

        Returns:
            str: The string representation of the refund request, including order ID and product ID.
        """
        return f"{self.order.orderId} - {self.product.productId}"
