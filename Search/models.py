from django.db import models

# Create your models here.
class Owner(models.Model):
    shopId=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=40,blank=True,null=True)
    shopName=models.CharField(max_length=50,blank=True,null=True)
    password=models.CharField(max_length=40,blank=True,null=True)
    username=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    def __str__(self):
        return str(self.name)+"-"+str(self.shopId) 
class Customer(models.Model):
    customerId=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=40,blank=True,null=True)
    username=models.CharField(max_length=40,blank=True,null=True)
    password=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    def __str__(self):
        return str(self.name)+"-"+str(self.customerId)

