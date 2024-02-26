from django.http import Http404
from django.shortcuts import render, redirect
from .models import Product, Review, Customer

def review(request, id):
    """
    View function for displaying and adding reviews for a product.

    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the product for which reviews are being viewed/added.

    Returns:
        HttpResponse: The HTTP response containing the rendered template.
    """

    try:
        # Get the product with the provided ID
        product = Product.objects.get(productId=int(id))
    except Product.DoesNotExist:
        # If the product does not exist, raise a 404 error
        raise Http404("Product does not exist")

    # Get all reviews for the product
    reviews = Review.objects.filter(product=product)

    # Get the customer associated with the logged-in user
    customer = Customer.objects.get(email=request.user.email)

    if 'add' in request.POST:
        # If a review is being added via POST request
        new_review_id = len(Review.objects.all()) + 1
        new_review = Review(
            customer=customer,
            product=product,
            reviewId=new_review_id,
            rating=len(request.POST.getlist('rating')),
            comment=request.POST.get('comment')
        )
        new_review.save()
        # Redirect to the same page after adding the review
        redirect_url = f"/review/{id}"
        return redirect(redirect_url)

    # Prepare the context to be passed to the template
    context = {
        'product': product,  # The product being reviewed
        'reviews': reviews   # All reviews for the product
    }

    # Render the template with the provided context
    return render(request, 'review.html', context)
