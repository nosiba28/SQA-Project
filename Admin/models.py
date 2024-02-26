from django.db import models
from Search.models import *
# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.categoryName) 
class Product(models.Model):
    productId=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    price=models.IntegerField(default=0,blank=True,null=True)
    shop=models.ForeignKey(Owner,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    offerPrice=models.IntegerField(default=0,null=True)
    offer=models.IntegerField(default=0,null=True)
    def __str__(self):
        return str(self.productId)+" - "+str(self.shop.shopId)   

