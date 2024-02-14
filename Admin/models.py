from django.db import models

# Creating Category model

class Category(models.Model):
    categoryName=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.categoryName) 

# Creating Product model

class Product(models.Model):
    productId=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    price=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return str(self.productId)+" - "+str(self.shop.shopId)   