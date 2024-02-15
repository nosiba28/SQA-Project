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