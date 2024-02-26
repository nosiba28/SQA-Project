from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.

    This class customizes the appearance and behavior of the Review model
    in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the list view of the admin interface.
        search_fields (tuple): The fields to include in the search functionality of the admin interface.
        list_filter (tuple): The fields to use for filtering records in the admin interface.
    """

    list_display = ('reviewId', 'product', 'customer', 'rating')
    search_fields = ('reviewId', 'product__name', 'customer__name')
    list_filter = ('rating',)
