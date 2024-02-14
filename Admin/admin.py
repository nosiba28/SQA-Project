from django.contrib import admin

# new branch created
#My admin product management task starts here
from .models import Product
from .models import Category

admin.site.register(Product)
admin.site.register(Category)

