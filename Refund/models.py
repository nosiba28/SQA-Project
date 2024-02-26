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
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Owner, Product, Order, indOrder, RefundRequest

class ManageRefundViewTestCase(TestCase):
    """
    Test cases for the manageRefund view.
    """

    def setUp(self):
        """
        Set up test data.
        """
        # Create users
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

        # Create owner
        self.owner = Owner.objects.create(shopId=1, name="Test Owner", email='test@example.com', username='testuser', password='password')

        # Create product
        self.product = Product.objects.create(productId=1, name='Test Product', price=10, shop=self.owner)

        # Create order
        self.order = Order.objects.create(customer=None, orderId=1, status=1)

        # Create individual order
        self.ind_order = indOrder.objects.create(date='2024-02-22', product=self.product, quantity=2, order=self.order, status=0)

        # Create refund request
        self.refund_request = RefundRequest.objects.create(reason='Defective product', product=self.product, order=self.order, status=0)

    def test_manage_refund_view(self):
        """
        Test the manageRefund view.
        """
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse('manageRefund'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manageRefund.html')

    def test_reject_refund_request(self):
        """
        Test rejecting a refund request.
        """
        client = Client()
        client.force_login(self.user)
        data = {
            'reject': 'reject',
            'order': self.order.id,
            'product': self.product.id,
        }
        response = client.post(reverse('manageRefund'), data)
        self.assertEqual(response.status_code, 302)  # Redirected after processing

    def test_accept_refund_request(self):
        """
        Test accepting a refund request.
        """
        client = Client()
        client.force_login(self.user)
        data = {
            'accept': 'accept',
            'order': self.order.id,
            'product': self.product.id,
        }
        response = client.post(reverse('manageRefund'), data)
        self.assertEqual(response.status_code, 302)  # Redirected after processing
