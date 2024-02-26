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
from Cart.models import *
from Admin.models import *
def order(request,id):
    order=Order.objects.get(orderId=int(id))
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
def payment(request,id,id2):
    order=Order.objects.get(orderId=int(id))    
    context={
        'id':id2,
        'order':order
    }
    return render(request,'payment.html',context)
def receipt(request,id):
    order=Order.objects.get(orderId=int(id))
    customer=Customer.objects.get(email=request.user.email)
    allProduct=indOrder.objects.filter(order=order)
    today=datetime.date.today()
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