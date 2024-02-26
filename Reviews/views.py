
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
def review(request,id):
    product=Product.objects.get(productId=int(id))
    reviews=Review.objects.filter(product=product)
    customer=Customer.objects.get(email=request.user.email)
    if 'add' in request.POST:
        newReviewId=len(Review.objects.filter())+1
        newReview=Review(
            customer=customer,
            product=product,
            reviewId=newReviewId,
            rating=len(request.POST.getlist('rating')),
            comment=request.POST.get('comment')
        )
        newReview.save()
        redirectUrl="/review/"+str(id)
        return redirect(redirectUrl)
    context={
        'reviews':reviews
    }

    return render(request,'review.html',context)