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
from .models import *
from Search.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import indOrder

# Create your views here.
# Cart function:
def cart(request):

    """
    View function for the cart page.

    This function handles the rendering of the cart page, including updating
    the quantities and total price of items in the cart.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered cart page.

    """
    # Getting the customer and order details
    customer=Customer.objects.get(email=request.user.email)
    order=Order.objects.get(customer=customer,status=0)
    allProduct=indOrder.objects.filter(order=order).order_by('product_id')

    # Post request for updating the cart's item
    if 'order' in request.POST:
        requestList=request.POST.getlist('product')
        totalSum=0
        # update the quantities and total price
        for o,i in zip(allProduct,requestList):
            prod=Product.objects.get(productId=o.product.productId)
            indOrde=indOrder.objects.get(order=order,product=prod)
           
            # Deleting the item if quantity is zero
            if int(i)==0: 
                indOrde.delete()
            else:
                indOrde.quantity=int(i)
                indOrde.save()
            totalSum+=(int(i)*prod.price)
        #updating the total price of the order
        order.total=totalSum
        order.save()
        redirectUrl='/order/'+str(order.orderId) 
        return redirect(redirectUrl)                              
    context={
        'allProduct':allProduct,
        'order':order
    }
    return render(request,'cart.html',context)

