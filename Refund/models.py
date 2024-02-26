from django.shortcuts import render, redirect
from .models import *  # Importing models from the same app
from Admin.models import *  # Importing models from the Admin app
from Cart.models import *   # Importing models from the Cart app

class RefundRequest(models.Model):
    """
    Represents a refund request.

    Attributes:
        reason (str): The reason for the refund request.
        product (Product): The product associated with the refund request.
        order (Order): The order associated with the refund request.
        status (int): The status of the refund request.
    """
    reason = models.CharField(max_length=100, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the RefundRequest instance.

        Returns:
            str: String representation of the refund request.
        """
        return str(self.order.orderId) + " - " + str(self.product.productId)


def manageRefund(request):
    """
    View function for managing refund requests.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTTP response.
    """
    # Retrieve the owner object based on the current user's email
    owner = Owner.objects.get(email=request.user.email)
    
    # Filter refund requests for products belonging to the shop owned by the current user
    refunds = RefundRequest.objects.filter(product__shop=owner, status=0)
    
    # Process form submissions
    if 'reject' in request.POST:
        # Retrieve order and product based on form data
        order = Order.objects.get(orderId=int(request.POST.get('order')))
        product = Product.objects.get(productId=int(request.POST.get('product')))
        
        # Update refund request and associated order status
        requestRefund = RefundRequest.objects.get(order=order, product=product)
        requestRefund.status = 1
        requestRefund.save()
        refundOrder = indOrder.objects.get(order=order, product=product)
        refundOrder.status = 3
        refundOrder.save()
        
        # Redirect to the refund management page after processing
        return redirect('/refund/manage')
    
    if 'accept' in request.POST:
        # Retrieve order and product based on form data
        order = Order.objects.get(orderId=int(request.POST.get('order')))
        product = Product.objects.get(productId=int(request.POST.get('product')))
        
        # Update refund request and associated order status
        requestRefund = RefundRequest.objects.get(order=order, product=product)
        requestRefund.status = 1
        requestRefund.save()
        refundOrder = indOrder.objects.get(order=order, product=product)
        refundOrder.status = 2
        refundOrder.save()
        
        # Redirect to the refund management page after processing
        return redirect('/refund/manage')
    
    # Prepare context to render the template
    context = {
        'refunds': refunds
    }
    
    # Render the manageRefund.html template with the context data
    return render(request, 'manageRefund.html', context)
