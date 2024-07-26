from django.shortcuts import render
from store.models import Product

def home(request):
    # Filtra los productos que están en oferta
    products_on_sale = Product.objects.filter(is_sale=True)
    
    # Pasa los productos en oferta al template
    return render(request, 'base/home.html', {
        'products_on_sale': products_on_sale,
    })
