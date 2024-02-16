import re  # Regular expression module
import json  # JSON module for working with JSON data
import datetime  # Module for working with dates and times
from decimal import Decimal  # Module for decimal arithmetic
from urllib import response  # Module for working with URLs
from io import BytesIO  # Module for working with binary data
from django.utils.html import strip_tags  # Django utility for stripping HTML tags
from django.core.files.storage import FileSystemStorage  # Django module for file storage
from django.shortcuts import render  # Django shortcut for rendering templates
from django.template.loader import get_template, render_to_string  # Django template loaders
from django.views import View  # Base class for Django views
from xhtml2pdf import pisa  # Module for converting HTML to PDF
from django.core.mail import send_mail, EmailMessage  # Django modules for sending emails
from django.conf import settings  # Django settings module
from django.http import HttpResponse  # Django HTTP response module
from django.shortcuts import redirect  # Django shortcut for redirecting
from django.utils import timezone  # Django module for handling timezones
from django.db import IntegrityError  # Django exception for database integrity errors
from django.contrib import messages  # Django messages framework for user feedback
import random  # Module for generating random numbers
from django.contrib.auth import authenticate, login, logout  # Django authentication modules
from django.contrib.auth.models import Group, User  # Django user and group models
from .models import *  # Importing all models from the current app
# from .models import Owner  # Importing specific model (commented out)
from Search.models import *  # Importing models from the 'Search' app
from django.contrib.auth.decorators import login_required  # Django decorator for requiring login

# CS: the first parameter in a view function should be called request.

# admin view method

def aadmin(request, id):
    """
    View method for managing admin tasks.
    Handles actions like adding, updating, removing, and viewing products.

    Args:
        request: HTTP request object.
        id: Shop ID.

    Returns:
        HTTP response or rendered template.
    """
    if 'ok' in request.POST:
        redirectUrl = ""
        if request.POST.get('manage') == '1':
            redirectUrl = "aadmin/addProduct/" + str(id)
            return redirect(redirectUrl)
        if request.POST.get('manage') == '2':
            redirectUrl = '/aadmin/updateProduct/' + str(id)
            return redirect(redirectUrl)
        if request.POST.get('manage') == '3':
            redirectUrl = '/aadmin/removeProduct/' + str(id)
            return redirect(redirectUrl)
        if request.POST.get('manage') == '4':
            redirectUrl = '/aadmin/allProduct/' + str(id)
            return redirect(redirectUrl)
    return render(request, 'aadmin.html')

# all products method

def allProduct(request, id):
    """
    View method for displaying all products of a shop.

    Args:
        request: HTTP request object.
        id: Shop ID.

    Returns:
        Rendered template displaying all products.
    """
    shop = Owner.objects.get(shopId=int(id))
    products = Product.objects.filter(shop=shop)
    context = {
        'shop': shop,
        'products': products
    }
    return render(request, 'allProduct.html', context)

# add product method

def addProduct(request, id):
    """
    View method for adding a new product.

    Args:
        request: HTTP request object.
        id: Shop ID.

    Returns:
        HTTP response or rendered template.
    """
    if 'add' in request.POST:
        shop = Owner.objects.get(shopId=int(id))
        newProductId = 0
        productList = Product.objects.filter()
        for product in productList:
            newProductId = max(newProductId, product.productId)
        newProductId += 1
        createProduct = Product(
            shop=shop,
            productId=newProductId,
            name=request.POST.get('name'),
            image=request.FILES.get('image'),
            desc=request.POST.get('desc'),
            price=int(request.POST.get('price'))
        )
        createProduct.save()
        redirectUrl = '/aadmin/' + str(id)
        return redirect(redirectUrl)
    return render(request, 'addProduct.html')

# update product method

def updateProduct(request, id):
    """
    View method for updating product details.

    Args:
        request: HTTP request object.
        id: Shop ID.

    Returns:
        HTTP response or rendered template.
    """
    if 'view' in request.POST:
        shop = Owner.objects.get(shopId=int(id))
        ifPresent = Product.objects.filter(shop=shop, productId=int(request.POST.get('id')))
        if not ifPresent:
            messages.error(request, "Such product does not exist !!!", extra_tags='error')
        else:
            product = Product.objects.get(shop=shop, productId=int(request.POST.get('id')))
            messages.success(request, {
                'name': product.name
            }, extra_tags='view')
            if 'update' in request.POST:
                product.name = request.POST.get('name')
                if request.FILES.get('image'):
                    product.image = request.FILES.get('image')
                product.desc = request.POST.get('desc')
                product.price = request.POST.get('price')
                product.save()
                redirectUrl = '/aadmin/' + str(id)
                return redirect(redirectUrl)

    return render(request, 'updateProduct.html')

# remove product method

def removeProduct(request, id):
    """
    View method for removing a product.

    Args:
        request: HTTP request object.
        id: Shop ID.

    Returns:
        HTTP response or rendered template.
    """
    shop = Owner.objects.get(shopId=int(id))
    if 'remove' in request.POST:
        ifPresent = Product.objects.filter(shop=shop, productId=int(request.POST.get('id')))
        if not ifPresent:
            messages.error(request, "Such product does not exist !!!", extra_tags='error')
        else:
            product = Product.objects.get(shop=shop, productId=int(request.POST.get('id')))
            product.delete()
            redirectUrl = '/aadmin/' + str(id)
            return redirect(redirectUrl)
    return render(request, 'removeProduct.html')

# view all product method

def allProduct(request, id):
    """
    View method for displaying all products of a shop.

    Args:
        request: HTTP request object.
        id: Shop ID.

    Returns:
        Rendered template displaying all products.
    """
    shop = Owner.objects.get(shopId=int(id))
    products = Product.objects.filter(shop=shop)
    context = {
        'shop': shop,
        'products': products
    }
    return render(request, 'allProduct.html', context)
