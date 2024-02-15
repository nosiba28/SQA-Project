from django.shortcuts import render

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
