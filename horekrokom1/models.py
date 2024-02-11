from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # Added missing field definition
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    availability = models.BooleanField();# Added missing field definition
    description = models.TextField()

class Order(models.Model):
    order_no = models.AutoField(primary_key=True)
    order_state = models.CharField(max_length=100)

class Transaction(models.Model):
    tracking_id = models.AutoField(primary_key=True)  # Corrected field name
    date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_no = models.ForeignKey(Order, on_delete=models.CASCADE)

class cart(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)   
    quantity = models.IntegerField()
    class Meta:
        unique_together = ('customer_id', 'product_id')
    

    

