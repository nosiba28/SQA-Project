from django.db import models
from Admin.models import *
from Cart.models import *

# Create your models here.

class RefundRequest(models.Model):
    """
    A class representing refund request for a specific product in an order.

    Attributes:
        reason (str): The reason for the refund request
        product (ForeignKey): A reference to the Product associated with the refund request
        order (ForeignKey): A reference to the Order associated with the refund request
        status (int): The status of the refund request (0 - pending, 1 - approved, 2 - rejected)
    """

    reason=models.CharField(max_length=100,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=0)

    def __str__(self):
        """
        A method that returns string containing the order ID and product ID.
        """
        return str(self.order.orderId)+" - "+str(self.product.productId) 