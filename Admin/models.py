from django.db import models

class Category(models.Model):
    """
    Model for product category.
    
    Fields:
        categoryName (CharField): Name of the category.
    """

    categoryName = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the Category object.
        
        Returns:
            str: Category name.
        """
        return str(self.categoryName) 

class Product(models.Model):
    """
    Model for product.
    
    Fields:
        productId (IntegerField): Unique identifier for the product.
        name (CharField): Name of the product.
        image (ImageField): Image associated with the product.
        desc (CharField): Description of the product.
        price (IntegerField): Price of the product.
    """
    

    productId = models.IntegerField(default=0, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True, default=None)  # Allow null values
    desc = models.CharField(max_length=100, blank=True, null=True, default=None)
    price = models.IntegerField(default=0, blank=True, null=True)
    shop = models.CharField(max_length=50, blank=True, null=True)  # Assuming shop is a local field

    def __str__(self):
        """
        Returns a string representation of the Product object.
        
        Returns:
            str: Concatenation of productId and shop ID.
        """
        return f"{self.productId} - {self.shop}"
