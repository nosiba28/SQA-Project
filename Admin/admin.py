from django.contrib import admin

# New branch created
# My admin product management task starts here

# Importing Product and Category models from current directory
from .models import Product
from .models import Category

# Registering Product and Category models with the Django admin site
admin.site.register(Product)
admin.site.register(Category)
