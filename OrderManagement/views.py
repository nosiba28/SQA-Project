# Import necessary modules and packages
import re
import json
import datetime
from decimal import Decimal
from urllib import response
from io import BytesIO
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string
from django.views import View
from xhtml2pdf import pisa
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.db import IntegrityError
from django.contrib import messages
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from .models import *  # Importing models from the same app
from Search.models import *  # Importing models from another app
from django.contrib.auth.decorators import login_required
from Cart.models import *
from Admin.models import *


# Define a view for handling orders
def order(request, id):
    # Retrieve the order object based on the provided id
    order = Order.objects.get(orderId=int(id))

    # Handle different payment options
    if request.POST.get('pay') == '1':
        redirectUrl = '/order/payment/' + str(id) + '/' + str(1)
        return redirect(redirectUrl)
    if request.POST.get('pay') == '2':
        redirectUrl = '/order/payment/' + str(id) + '/' + str(2)
        return redirect(redirectUrl)
    if request.POST.get('pay') == '3':
        redirectUrl = '/order/payment/' + str(id) + '/' + str(3)
        return redirect(redirectUrl)
    if request.POST.get('pay') == '4':
        return redirect('/cart')

    # Prepare context to render the order.html template
    context = {
        'order': order
    }
    return render(request, 'order.html', context)


# Define a view for handling payments
def payment(request, id, id2):
    # Retrieve the order object based on the provided id
    order = Order.objects.get(orderId=int(id))

    # Prepare context to render the payment.html template
    context = {
        'id': id,
        'order': order
    }
    return render(request, 'payment.html', context)


# Define a view for generating receipts
def receipt(request, id):
    # Retrieve the order object based on the provided id
    order = Order.objects.get(orderId=int(id))

    # Retrieve customer information based on the current user's email
    customer = Customer.objects.get(email=request.user.email)

    # Retrieve all individual ordered products for the current order
    allProduct = indOrder.objects.filter(order=order)

    # Get today's date
    today = datetime.date.today()

    # Handle form submissions for confirming or going back
    if 'confirm' in request.POST:
        # Update the order status to confirmed (status=1)
        order.status = 1
        order.save()
        return redirect('/product')  # Redirect to product page after confirming order
    if 'back' in request.POST:
        return redirect('/cart')  # Redirect back to cart if user chooses to go back

    # Prepare context to render the receipt.html template
    context = {
        'order': order,
        'allProduct': allProduct,
        'customer': customer,
        'date': today
    }
    return render(request, 'receipt.html', context)
