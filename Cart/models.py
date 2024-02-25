from django.db import models
import datetime
# Create your models here.
from Search.models import *
from Admin.models import *
class Order(models.Model):
    # shop=models.ForeignKey(Owner,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    orderId=models.IntegerField(default=0,null=True,blank=True)
    status=models.IntegerField(default=0,null=True,blank=True)
    total=models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return str(self.orderId)
class indOrder(models.Model):
    date=models.DateField(null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1,null=True,blank=True)
    status=models.IntegerField(default=0,null=True)
    def __str__(self):
        return str(self.order.orderId)+" - "+str(self.product.productId)   

