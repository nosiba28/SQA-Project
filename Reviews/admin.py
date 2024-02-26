from django.contrib import admin
from .models import *

# Register your models here.

# Registering all models from the current application for administration in the Django admin site.
admin.site.register(Review)
