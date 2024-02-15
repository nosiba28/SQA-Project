from django.shortcuts import render
from .models import Product
from .models import Category
from django.http import HttpResponse
from django.shortcuts import redirect


# CS: the first parameter in a view function should be called request.

# admin view method

def aadmin(request,id):
    if 'ok' in request.POST:
        redirectUrl=""
        if request.POST.get('manage')=='1':
            redirectUrl="/aadmin/addProduct/"+str(id)
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



def allProduct(request,id):
    shop=Owner.objects.get(shopId=int(id))
    products=Product.objects.filter(shop=shop)
    context={
        'shop':shop,
        'products':products
    }
    return render(request,'allProduct.html',context)

