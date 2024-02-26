from django.db import models
from Admin.models import Product, Customer  # Importing Product and Customer models from Admin app
from Search.models import Product  # Importing Product model from Search app

# Define your models here.
class Review(models.Model):
    """
    Model to represent a review for a product.

    Attributes:
        reviewId (IntegerField): The ID of the review.
        comment (CharField): The comment associated with the review.
        product (ForeignKey): The product being reviewed (related to Product model).
        customer (ForeignKey): The customer who submitted the review (related to Customer model).
        rating (IntegerField): The rating given in the review.
    """
    reviewId = models.IntegerField(default=0, null=True)
    comment = models.CharField(max_length=100, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0, null=True)

    def __str__(self):
        """
        Method to return a string representation of the review.

        Returns:
            str: A string representation of the review, consisting of review ID and product ID.
        """
        return str(self.reviewId) + " - " + str(self.product.productId)
