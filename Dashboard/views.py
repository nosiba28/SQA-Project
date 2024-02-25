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
View function for rendering the dashboard page

It retrieves data related to orders and sales to display on the dashboard
calculates various metrics such as total sales, sales per product, and sales per month
The data is then passed to the dashboard template for visualization
"""
def dashboard(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponse
        HTTP response that renders the dashboard page
    """
    
    # Retrieve the admin (owner) associated with the logged-in user
    admin=Owner.objects.get(email=request.user.email)

    # Retrieve all individual orders associated with the admin's shop
    orders=indOrder.objects.filter(product__shop=admin,order__status=1).order_by('date')
    #orders=indOrder.objects.filter(product__shop=admin).order_by('date')

    # Initialize dictionaries and lists to store data for visualization
    queryDict={}
    lineLabels=[]
    lineData=[]
    pieLabels=[]
    pieData=[]
    monthDict={}
    productDict={}
    monthLabels=[]
    monthData=[]

    # Define a dictionary mapping month numbers to month names
    months={
        1:"January",
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'Novermber',
        12:'December'
    }

    # Process orders to calculate sales data
    for o in orders:
        productDict[o.product.name]=0
        ss=str(o.date.year)+"-"+months[o.date.month]
        monthDict[ss]=0
        queryDict[o.date]=0
   
    for o in orders:
        ss=str(o.date.year)+"-"+months[o.date.month]
        monthDict[ss]+=(o.quantity*o.product.offerPrice)
        productDict[o.product.name]+=o.quantity
        queryDict[o.date]+=(o.quantity*o.product.offerPrice)

    # Prepare data for visualization
    for o in queryDict:
        lineLabels.append(str(o))
        lineData.append(queryDict[o])

    for o in productDict:
        pieLabels.append(o)
        pieData.append(productDict[o])

    for o in monthDict:
        monthLabels.append(o)
        monthData.append(monthDict[o])

    # Create context dictionary to pass data to the template
    context={
        'orders':orders,
        'lineLabels':lineLabels,
        'lineData':lineData,
        'pieLabels':pieLabels,
        'pieData':pieData,
        'monthLabels':monthLabels,
        'monthData':monthData
        
    }

    # Render the dashboard template with the data
    return render(request,'dashboard.html',context)