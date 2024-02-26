from django.db import models
from Search.models import *
from Admin.models import *
# Create your models here.

class Wishlist(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.product.productId)+" - "+str(self.customer.customerId)