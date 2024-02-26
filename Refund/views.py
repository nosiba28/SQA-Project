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
from Cart.models import *
from Wishlist.models import *
from Admin.models import *
from django.contrib.auth.decorators import login_required
 
#write your views here

"""
Order history page

This function retrieves the order history for the current user and categorizes
the orders into two lists: refundable orders and regular orders. It also processes
refund requests submitted by users
"""

def orderHistory(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponse
        HTTP response that renders order history page
    """
    customer=Customer.objects.get(email=request.user.email)
    orders=Order.objects.filter(customer=customer,status=1)
    orderList=[]

    # Retrieve all individual orders associated with the customer
    for o in orders:
        indOrders=indOrder.objects.filter(order=o)
        for i in indOrders:
            orderList.append(i)

    refundList=[]
    regularList=[]

    # Process refund requests submitted by users
    if 'apply' in request.POST:
        order=Order.objects.get(customer=customer,status=1,
                                orderId=int(request.POST.get('order')))
        product=Product.objects.get(productId=int(request.POST.get('apply')))
        createRequest=RefundRequest(
            reason=request.POST.get('reason'),
            order=order,
            product=product
        )
        createRequest.save()
        oa=indOrder.objects.get(order=order,product=product)
        oa.status=1
        oa.save()
        return redirect('/refund')

    # Categorize orders into refundable and regular orders based on their status and date
    for o in orderList:
        today=datetime.datetime.today().date()
        diff=(today-o.date).days
        if diff<=6 and o.status<=2:
            refundList.append(o)
        else:
            regularList.append(o)

    context={
        'refundList':refundList,
        'regularList':regularList
    }
    
    # Render the order history page with the categorized orders
    return render(request,'refund.html',context)

