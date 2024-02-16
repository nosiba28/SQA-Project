from django.db import models

# Create your models here.
class Owner(models.Model):
    """
    A class to represent an Owner.

    Attributes:
        shopId (IntegerField): The unique identifier for the owner's shop.
        name (CharField): The name of the owner.
        email (EmailField): The email address of the owner.
        shopName (CharField): The name of the owner's shop.
        password (CharField): The password of the owner.
        username (CharField): The username of the owner.
        image (ImageField): An image representing the owner (optional).
        desc (CharField): A description of the owner (optional).
    """
    shopId=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=40,blank=True,null=True)
    shopName=models.CharField(max_length=50,blank=True,null=True)
    password=models.CharField(max_length=40,blank=True,null=True)
    username=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    def __str__(self):
        """
        A method that return a string consisting of the Owner's name and shop ID
        """
        return str(self.name)+"-"+str(self.shopId) 
    
class Customer(models.Model):
    """
    A class to represent a Customer.

    Attributes:
        customerId (IntegerField): The unique identifier for the customer.
        name (CharField): The name of the customer.
        email (EmailField): The email address of the customer.
        username (CharField): The username of the customer.
        password (CharField): The password of the customer.
        image (ImageField): An image representing the customer (optional).
        desc (CharField): A description of the customer (optional).
    """
    customerId=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=40,blank=True,null=True)
    username=models.CharField(max_length=40,blank=True,null=True)
    password=models.CharField(max_length=40,blank=True,null=True)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    def __str__(self):
        """
        A method that returns the Customer name and customer ID
        """
        return str(self.name)+"-"+str(self.customerId)


