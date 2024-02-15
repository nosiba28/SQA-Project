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
from .models import Owner
from Search.models import *
from django.contrib.auth.decorators import login_required

# CS: the first parameter in a view function should be called request.

# admin view method

def aadmin(request,id):
    if 'ok' in request.POST:
        redirectUrl=""
        if request.POST.get('manage')=='1':
            redirectUrl="aadmin/addProduct/"+str(id)
            return redirect(redirectUrl)
        if request.POST.get('manage')=='2':
            redirectUrl='/aadmin/updateProduct/'+str(id)
            return redirect(redirectUrl)
        if request.POST.get('manage')=='3':
            redirectUrl='/aadmin/removeProduct/'+str(id)
            return redirect(redirectUrl)
        if request.POST.get('manage')=='4':
            redirectUrl='/aadmin/allProduct/'+str(id)
            return redirect(redirectUrl)
    return render(request,'aadmin.html')

#all products method

def allProduct(request,id):
    shop=Owner.objects.get(shopId=int(id))
    products=Product.objects.filter(shop=shop)
    context={
        'shop':shop,
        'products':products
    }
    return render(request,'allProduct.html',context)

#add product method

def addProduct(request,id):
    if 'add' in request.POST:
        shop=Owner.objects.get(shopId=int(id))
        newProductId=0
        productList=Product.objects.filter()
        for product in productList:
            newProductId=max(newProductId,product.productId)
        newProductId+=1
        createProduct=Product(
            shop=shop,
            productId=newProductId,
            name=request.POST.get('name'),
            image=request.FILES.get('image'),
            desc=request.POST.get('desc'),
            price=int(request.POST.get('price'))
        )
        createProduct.save()
        redirectUrl='/aadmin/'+str(id)
        return redirect(redirectUrl)
    return render(request,'addProduct.html')

# update product method

def updateProduct(request,id):
    if 'view' in request.POST:
        shop=Owner.objects.get(shopId=int(id))
        ifPresent=Product.objects.filter(shop=shop,productId=int(request.POST.get('id')))
        if not ifPresent:
            messages.error(request, "Such product does not exist !!!",extra_tags='error')
        else:
            product=Product.objects.get(shop=shop,
                                        productId=int(request.POST.get('id')))
            messages.success(request,{
                'name':product.name
            },extra_tags='view')
            if 'update' in request.POST:
                product.name=request.POST.get('name')
                if request.FILES.get('image'):
                    product.image=request.FILES.get('image')
                product.desc=request.POST.get('desc')
                product.price=request.POST.get('price')
                product.save()
                redirectUrl='/aadmin/'+str(id)
                return redirect(redirectUrl)

    return render(request,'updateProduct.html')

#remove product method

def removeProduct(request,id):
    shop=Owner.objects.get(shopId=int(id))
    if 'remove' in request.POST:
        ifPresent=Product.objects.filter(shop=shop,productId=int(request.POST.get('id')))
        if not ifPresent:
            messages.error(request, "Such product does not exist !!!",extra_tags='error')
        else:
            product=Product.objects.get(shop=shop,productId=int(request.POST.get('id')))
            product.delete()
            redirectUrl='/aadmin/'+str(id)
            return redirect(redirectUrl)
    return render(request,'removeProduct.html')

# view all product method

def allProduct(request,id):
    shop=Owner.objects.get(shopId=int(id))
    products=Product.objects.filter(shop=shop)
    context={
        'shop':shop,
        'products':products
    }
    return render(request,'allProduct.html',context)