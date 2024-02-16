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
# The first parameter in a view function should be called request.

"""
Home page
This view renders the home page
"""

def home(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponse
        HTTP response that renders the home page
    """
    return render(request,'home.html')


"""
Login page
This view handles the login functionality
"""

def logIn(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponse
        HTTP response that renders the login page or redirects to another page
    """
    if 'login' in request.POST:
        # Check if user is an owner or a customer
        if request.POST.get('type')=='2':
            # Handling owner login
            ifPresent=Owner.objects.filter(email=request.POST.get('email'))
            if not ifPresent:
                # If email does not exist
                 messages.error(request, "Email does not exist!!",extra_tags='error')
            else:
                # If email exists, validate password
                owner=Owner.objects.get(email=request.POST.get('email'))
                if owner.password!=request.POST.get('password'):
                    messages.error(request, "Paswords do not match!!",extra_tags='error')
                else:
                    # Log in the owner and redirect to dashboard
                    login(request,authenticate(request,username=owner.username,password=owner.password))
                    redirectUrl="/aadmin/"+str(owner.shopId)
                    return redirect(redirectUrl)
        else:
            # Handling customer login
            ifPresent=Customer.objects.filter(email=request.POST.get('email'))
            if not ifPresent:
                 messages.error(request, "Email does not exist!!",extra_tags='error')
            else:
                customer=Customer.objects.get(email=request.POST.get('email'))
                if customer.password!=request.POST.get('password'):
                    messages.error(request, "Paswords do not match!!",extra_tags='error')
                else:
                    login(request,authenticate(request,username=customer.username,password=customer.password))
                    return redirect('/')
    return render(request,'logIn.html')


"""
Redirects to the login page after logging out
"""

def logOut(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponseRedirect
        Redirects to the login page.
    """
    logout(request)
    return redirect('/logIn')


"""
Register page
This view handles user registration
"""

def register(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponse
        HTTP response that renders the registration page or redirects to another page
    """
    if 'register' in request.POST:
        print(request.POST.get('type'))
        if request.POST.get('type')=='2':
            # Handling owner registration
            ifPresent=Owner.objects.filter(email=request.POST.get('email'))
            if not ifPresent:
                newShopId=len(Owner.objects.filter())+1
                createOwner=Owner(
                    name=request.POST.get('name'),
                    shopName=request.POST.get('shop'),
                    shopId=newShopId,
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('pass'),
                )
                createOwner.save()
                user=User.objects.create_user(username=createOwner.username,email=createOwner.email,password=createOwner.password)
                return redirect('/logIn')

            else:
                messages.error(request, "Email already exists!!",extra_tags='error')
        else:
            # Handling customer registration
            newCustomerId=len(Customer.objects.filter())+1
            ifPresent=Customer.objects.filter(email=request.POST.get('email'))
            if not ifPresent:
                createCustomer=Customer(
                    customerId=newCustomerId,
                    name=request.POST.get('name'),
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('pass'),
                )
                createCustomer.save()
                user=User.objects.create_user(username=createCustomer.username,email=createCustomer.email,password=createCustomer.password)
                return redirect('/logIn')

            else:
                messages.error(request, "Email already exists!!",extra_tags='error')

    return render(request,'register.html')


"""
Product page
This view renders the product page
handles product addition to the cart/wishlist
search and filter products based on certain criteria
"""

def product(request):
    """
    Parameters
    ----------
    request : HttpRequest
        HTTP request object

    Returns
    -------
    return : HttpResponse
        HTTP response that renders the product page with updated information
    """
    customer=Customer.objects.get(email=request.user.email)
    allProduct=Product.objects.filter()
    currentCart=Order.objects.filter(customer=customer,status=0)
    shopList=Owner.objects.filter()
    categoryList=Category.objects.filter()

    # If there is no active cart for the customer, create a new one
    if not currentCart:
        newOrderId=len(Order.objects.filter())+1
        currentCart=Order(
            customer=customer,
            orderId=newOrderId
        )
        currentCart.save()
    # Get the current active cart for the customer
    cart=Order.objects.get(customer=customer,status=0)

    # Handle adding products to the cart
    if 'add' in request.POST:
        product=Product.objects.get(productId=int(request.POST.get('add')))
        addProduct=indOrder(
            product=product,
            order=cart  
        )
        cart.total+=product.price
        cart.save()
        addProduct.save()
        return redirect('/product')
    
    # Handle adding products to the wishlist
    if 'wishlist' in request.POST:
        product=Product.objects.get(productId=int(request.POST.get('wishlist')))
        createWish=Wishlist(
            customer=customer,
            product=product
        )
        createWish.save()
        return redirect('/product')
    
    # Handle product search
    if 'search' in request.POST:
        # Filtering products based on search criteria
        filteredList=set()
        shops=request.POST.getlist('shops')
        categories=request.POST.getlist('category')
        newShop=shops
        newCategories=categories
        mi=int(request.POST.get('min'))
        ma=int(request.POST.get('max'))

        # If no shops selected, include all shops
        if not shops:
            shops=Owner.objects.values_list('shopId')
            for o in shops:
                newShop.append(o[0])

        # If no categories selected, include all categories
        if not categories:
            categories=Category.objects.values_list('categoryName')
            for o in categories:
                newCategories.append(o[0])

        # Filter products based on shop and price range
        for o in newShop:
            for i in allProduct:
                if int(o)==i.shop.shopId and (i.price >= mi and i.price <= ma):
                    prod=Product.objects.get(productId=i.productId,shop__shopId=i.shop.shopId)
                    filteredList.add(prod)
        newFilteredList=set()

        # Filter products based on category and price range
        for o in newCategories:
            for i in filteredList:
                if o == i.category.categoryName and (i.price >= mi and i.price <= ma):
                    prod=Product.objects.get(productId=i.productId,shop__shopId=i.shop.shopId)
                    newFilteredList.add(prod)

        # Sort the filtered products based on price
        if request.POST.get('sort')=='1':
            newFilteredList=list(newFilteredList)
            newFilteredList.sort(key=lambda x:x.price)
        else:
            newFilteredList=list(newFilteredList)
            newFilteredList.sort(key=lambda x:x.price,reverse=True)

        # Create a dictionary to store product data
        queryDict={}
        for o in newFilteredList:
            queryDict[o]=(0,0)

        # Update the flags for products already in cart or wishlist
        cartProducts=indOrder.objects.filter(order=cart)
        wishList=Wishlist.objects.filter(customer=customer)
        for o in newFilteredList:
            for i in cartProducts:
                if o.productId==i.product.productId:
                    queryDict[o]=(1,0)
        
        for o in newFilteredList:
            for i in wishList:
                if o.productId==i.product.productId:
                    queryDict[o]=(queryDict[o][0],1)
        for o in queryDict:
            print(queryDict[o][0])
        context={
            'allProduct':allProduct,
             'shopList':shopList,
             'categoryList':categoryList,
             'queryDict':queryDict
        }
        return render(request,'product.html',context)
    
    # Prepare data for rendering the product page without search
    queryDict={}
    for o in allProduct:
        queryDict[o]=(0,0)
    cartProducts=indOrder.objects.filter(order=cart)
    wishList=Wishlist.objects.filter(customer=customer)
    for o in allProduct:
        for i in cartProducts:
            if o.productId==i.product.productId:
                queryDict[o]=(1,0)
    
    for o in allProduct:
        for i in wishList:
            if o.productId==i.product.productId:
                queryDict[o]=(queryDict[o][0],1)
    context={
        'allProduct':allProduct,
        'shopList':shopList,
        'categoryList':categoryList,
        'queryDict':queryDict
    }
    return render(request,'product.html',context)