
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
# Create your views here.
def wishlist(request):
    
    customer=Customer.objects.get(email=request.user.email)
    wishList=Wishlist.objects.filter(customer=customer)
    cart=Order.objects.get(customer=customer,status=0)
    queryDict={}
    for o in wishList:
        queryDict[o.product]=0
    allProduct=indOrder.objects.filter(order=cart)
    for o in allProduct:
        if queryDict.get(o.product) != None:
            queryDict[o.product]=1

    if 'remove' in request.POST:
        product=Product.objects.get(productId=request.POST.get('remove'))
        wish=Wishlist.objects.get(customer=customer,product=product)
        wish.delete()
        return redirect('/wishlist')
    if 'addcart' in request.POST:
        product=Product.objects.get(productId=int(request.POST.get('addcart')))
        addProduct=indOrder(
            product=product,
            order=cart  
        )
        cart.total+=product.offerPrice
        cart.save()
        addProduct.save()
        return redirect('/cart')
    context={
        'wishList':queryDict
    }
    return render(request,'wishlist.html',context)