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
def cart(request):
    customer=Customer.objects.get(email=request.user.email)
    order=Order.objects.get(customer=customer,status=0)
    allProduct=indOrder.objects.filter(order=order).order_by('product_id')
    if 'order' in request.POST:
        requestList=request.POST.getlist('product')
        totalSum=0
        for o,i in zip(allProduct,requestList):
            prod=Product.objects.get(productId=o.product.productId)
            indOrde=indOrder.objects.get(order=order,product=prod)
            if int(i)==0:
                indOrde.delete()
            else:
                indOrde.quantity=int(i)
                indOrde.save()
            totalSum+=(int(i)*prod.offerPrice)
        order.total=totalSum
        order.save()
        redirectUrl='/order/'+str(order.orderId)
        return redirect(redirectUrl)                         
    context={
        'allProduct':allProduct,
        'order':order
    }
    return render(request,'cart.html',context)

