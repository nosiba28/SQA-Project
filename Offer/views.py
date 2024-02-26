
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

def offer(request):
    owner=Owner.objects.get(email=request.user.email)
    products=Product.objects.filter(shop=owner)
    categories=Category.objects.filter()
    if 'apply' in request.POST:
        categoryList=request.POST.getlist('category')
        for i in categoryList:
            for o in products:
                if o.category.categoryName==i:
                    product=Product.objects.get(productId=o.productId)
                    product.offer=int(request.POST.get('disc'))
                    product.save()
                    product.offerPrice=product.price-(product.price*(product.offer/100))
                    product.save()
        return redirect('/offer')
    if 'all' in request.POST:
        for o in products:
            product=Product.objects.get(productId=o.productId)
            product.offer=int(request.POST.get('disc'))
            product.save()
            product.offerPrice=product.price-(product.price*(product.offer/100))
            product.save()
        return redirect('/offer')
    if 'discard' in request.POST:
        for o in products:
            product=Product.objects.get(productId=o.productId)
            product.offer=0
            product.offerPrice=product.price
            product.save()
        return redirect('/offer')
    if 'ind' in request.POST:
        product=Product.objects.get(shop=owner,productId=int(request.POST.get('ind')))
        product.offer=int(request.POST.get('discount'))
        product.save()
        product.offerPrice=product.price-(product.price*(product.offer/100))
        product.save()
        return redirect('/offer')
    context={
        'categories':categories,
        'products':products
    }
    return render(request,'offer.html',context)