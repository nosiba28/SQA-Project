from django.db import models
from Search.models import *
from Admin.models import *
# Create your models here.
#Order Model
class Order(models.Model):
    """
    Represents an order placed by a customer.

    Attributes:
        customer (Customer): The customer who placed the order.
        orderId (int): The unique identifier for the order.
        status (int): The status of the order.
        total (int): The total amount of the order.
    """
    #foreign key
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    #Model's Fields 
    orderId=models.IntegerField(default=0,null=True,blank=True)
    status=models.IntegerField(default=0,null=True,blank=True)
    total=models.IntegerField(default=0,null=True,blank=True)

    """
    Returns a string which represent the order.

    Returns:
        str: The string representation of the order.
    
    """
    def __str__(self):
        return str(self.orderId)
    
# Individual Order Model
class indOrder(models.Model):
    """
    Represents an individual product within an order.

    Attributes:
        product (Product): The product included in the order.
        order (Order): The order to which the product belongs.
        quantity (int): The quantity of the product in the order.
    """
    #Foreign keys
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    #Model'e field
    quantity=models.IntegerField(default=1,null=True,blank=True)

    """
    returns a string concatenating the "orderId" of the related order instance and "productId" of the related product instance.

    Returns:
        str: The string representation of the individual order

    """
    def __str__(self):
        return str(self.order.orderId)+" - "+str(self.product.productId)   

