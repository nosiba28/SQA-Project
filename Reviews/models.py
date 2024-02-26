from django.db import models
from Admin.models import Product
from Search.models import Customer

class Review(models.Model):
    """
    Model representing a review for a product.

    Each review has a review ID, comment, rating, associated product, and customer.

    Attributes:
        reviewId (IntegerField): The unique identifier for the review.
        comment (CharField): The comment provided by the customer for the review.
        product (ForeignKey): The product associated with the review.
        customer (ForeignKey): The customer who submitted the review.
        rating (IntegerField): The rating given by the customer for the product.
    """

    reviewId = models.IntegerField(default=0, null=True)
    comment = models.CharField(max_length=100, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0, null=True)

    def __str__(self):
        """
        String representation of the review.

        Returns:
            str: A string representation of the review in the format "<reviewId> - <productId>".
        """
        return f"{self.reviewId} - {self.product.productId}"
