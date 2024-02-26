from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Review, Customer

def review(request, id):
    """
    View function to display and add reviews for a product.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the product for which reviews are being viewed/added.

    Returns:
        HttpResponse: The HTTP response object rendering the review template.
    """
    # Retrieve the product based on the provided ID
    product = Product.objects.get(productId=int(id))

    # Retrieve all reviews for the product
    reviews = Review.objects.filter(product=product)

    # Retrieve the current customer
    customer = Customer.objects.get(email=request.user.email)

    # Process POST request to add a new review
    if 'add' in request.POST:
        # Generate a new review ID
        new_review_id = len(Review.objects.all()) + 1

        # Create a new review object
        new_review = Review(
            customer=customer,
            product=product,
            reviewId=new_review_id,
            rating=len(request.POST.getlist('rating')),
            comment=request.POST.get('comment')
        )

        # Save the new review
        new_review.save()

        # Redirect to the review page for the same product
        redirect_url = "/review/" + str(id)
        return redirect(redirect_url)

    # Prepare the context data to be passed to the template
    context = {
        'reviews': reviews
    }

    # Render the review template with the provided context
    return render(request, 'review.html', context)
