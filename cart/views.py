from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseBadRequest
from store.models import Product
from .cart import Cart

# Create your views here.
def cart_summary(request):
    return render(request, "cart/cart_summary.html", {})


def cart_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if not product_id:
            return HttpResponseBadRequest('No product_id provided')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponseBadRequest('Product does not exist')

        cart = Cart(request)
        cart.add(product=product)

        return JsonResponse({'Product Name': product.name})
    return HttpResponseBadRequest('Invalid request method')
    
def cart_delete(request):
    return render(request, "cart/cart_delete.html", {})

def cart_update(request):
    return render(request, "cart/cart_update.html", {})