from django.db import models
from Admin.models import *
from Search.models import *
# Create your models here.
class Review(models.Model):
    reviewId=models.IntegerField(default=0,null=True)
    comment=models.CharField(max_length=100,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    rating=models.IntegerField(default=0,null=True)
    def __str__(self):
        return str(self.reviewId)+" - "+str(self.product.productId)