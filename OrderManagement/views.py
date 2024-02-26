import re
import json
import datetime
from decimal import Decimal
from urllib import response
from io import BytesIO
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.template.loader import get_template,render_to_string
from django.views import View
from xhtml2pdf import pisa
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.db import IntegrityError
from django.contrib import messages
import json
import random
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
from .models import *  # Importing models from the same directory
from Search.models import *  # Importing models from the Search directory
from django.contrib.auth.decorators import login_required
from Cart.models import *  # Importing models from the Cart directory
from Admin.models import *  # Importing models from the Admin directory

# View for handling orders


"""
    View function for handling orders.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - id (int): The ID of the order.

    Returns:
    - HttpResponse: A rendered HTML response displaying order details.
    """

def order(request,id):
    # Getting the order object based on the provided id
    order=Order.objects.get(orderId=int(id))
    # Checking if the payment method is selected and redirecting accordingly
    if request.POST.get('pay')=='1':
        redirectUrl='/order/payment/'+str(id)+'/'+str(1)
        return redirect(redirectUrl)
    if request.POST.get('pay')=='2':
        redirectUrl='/order/payment/'+str(id)+'/'+str(2)
        return redirect(redirectUrl)
    if request.POST.get('pay')=='3':
        redirectUrl='/order/payment/'+str(id)+'/'+str(3)
        return redirect(redirectUrl)
    if request.POST.get('pay')=='4':
        return redirect('/cart')
    context={
        'order':order
    }
    return render(request,'order.html',context)

# View for handling payments
def payment(request,id,id2):
    # Getting the order object based on the provided id
    order=Order.objects.get(orderId=int(id))    
    context={
        'id':id2,
        'order':order
    }
    return render(request,'payment.html',context)

# View for generating receipts
def receipt(request,id):
    # Getting the order object based on the provided id
    order=Order.objects.get(orderId=int(id))
    # Getting the customer object based on the logged-in user's email
    customer=Customer.objects.get(email=request.user.email)
    # Getting all individual products for the order
    allProduct=indOrder.objects.filter(order=order)
    # Getting the current date
    today=datetime.date.today()
    # Handling form submission for confirmation or going back to cart
    if 'confirm' in request.POST:
        order.status=1
        today=datetime.datetime.today().date()
        for o in allProduct:
            product=Product.objects.get(productId=o.product.productId)
            saveOrder=indOrder.objects.get(order=order,product=product)
            saveOrder.date=today
            saveOrder.save()
        order.save()
        return redirect('/product')
    if 'back' in request.POST:
        return redirect('/cart')
    context={
        'order':order,
        'allProduct':allProduct,
        'customer':customer,
        'date':today
    }
    return render(request,'receipt.html',context)
