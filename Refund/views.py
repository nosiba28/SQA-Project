import re
import json
import datetime
from decimal import Decimal
from urllib import response
from io import BytesIO
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.views import View
from xhtml2pdf import pisa
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.db import IntegrityError
from django.contrib import messages
import json
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from .models import *  # Importing models from the current app
from Search.models import *  # Importing models from the Search app
from Cart.models import *  # Importing models from the Cart app
from Wishlist.models import *  # Importing models from the Wishlist app
from Admin.models import *  # Importing models from the Admin app
from django.contrib.auth.decorators import login_required

@login_required
def manageRefund(request):
    """
    View function for managing refund requests.

    Retrieves refund requests related to the owner's shop,
    processes form submissions for accepting or rejecting refunds,
    and renders the 'manageRefund.html' template.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered template.
    """
    # Retrieve the owner object based on the current user's email
    owner = Owner.objects.get(email=request.user.email)
    
    # Retrieve refund requests related to the owner's shop
    refunds = RefundRequest.objects.filter(product__shop=owner, status=0)
    
    # Process form submissions
    if 'reject' in request.POST:
        # Retrieve order and product based on form data
        order = Order.objects.get(orderId=int(request.POST.get('order')))
        product = Product.objects.get(productId=int(request.POST.get('product')))
        
        # Update refund request and associated order status for rejection
        requestRefund = RefundRequest.objects.get(order=order, product=product)
        requestRefund.status = 1
        requestRefund.save()
        refundOrder = indOrder.objects.get(order=order, product=product)
        refundOrder.status = 3
        refundOrder.save()
        
        # Redirect to the refund management page after processing
        return redirect('/refund/manage')
    
    if 'accept' in request.POST:
        # Retrieve order and product based on form data
        order = Order.objects.get(orderId=int(request.POST.get('order')))
        product = Product.objects.get(productId=int(request.POST.get('product')))
        
        # Update refund request and associated order status for acceptance
        requestRefund = RefundRequest.objects.get(order=order, product=product)
        requestRefund.status = 1
        requestRefund.save()
        refundOrder = indOrder.objects.get(order=order, product=product)
        refundOrder.status = 2
        refundOrder.save()
        
        # Redirect to the refund management page after processing
        return redirect('/refund/manage')
    
    # Prepare context to render the template
    context = {
        'refunds': refunds
    }
    
    # Render the manageRefund.html template with the context data
    return render(request, 'manageRefund.html', context)
