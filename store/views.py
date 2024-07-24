from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Category



def product(request, pk):
    """Vista para mostrar los detalles de un producto."""
    product = get_object_or_404(Product, id=pk)
    return render(request, 'store/product.html', {'product': product})

def category(request, foo):
    """Vista para mostrar productos por categoría."""
    foo = foo.replace('-', ' ')
    categories = Category.objects.all()
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {'products': products, 'category': category, 'categories': categories})
    except Category.DoesNotExist:
        messages.error(request, "¡Esta categoría no existe!")
        return redirect('home')
