from django.contrib import admin

# new branch created
#My admin product management task starts here

from .models import *
admin.site.register(Product)
