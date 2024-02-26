from django.db import models
from Admin.models import *
from Cart.models import *
# Create your models here.
class RefundRequest(models.Model):
    reason=models.CharField(max_length=100,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=0)
    def __str__(self):
        return str(self.order.orderId)+" - "+str(self.product.productId) 