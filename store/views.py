from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Category, Subcategory
from django.contrib import messages
from django.db.models import Q




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

def subcategory(request, foo):
    """Vista para mostrar productos por subcategoría."""
    foo = foo.replace('-', ' ')
    categories = Category.objects.all()
    try:
        subcategory = Subcategory.objects.get(name=foo)
        products = Product.objects.filter(subcategory=subcategory)
        return render(request, 'store/subcategory.html', {'products': products, 'subcategory': subcategory, 'categories': categories})
    except Subcategory.DoesNotExist:
        messages.error(request, "¡Esta subcategoría no existe!")
        
        

    
        
        
        
def search(request):
    """Vista para buscar un producto."""
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        if not searched:
            messages.error(request, "¡Por favor ingresa un término de búsqueda!")
            return redirect(request.META.get('HTTP_REFERER'))  # Redirige a la página anterior
        
        # Consultar el modelo de base de datos del producto usando Q
        products = Product.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        
        if not products.exists():
            messages.error(request, "¡No se encontraron productos que coincidan con tu búsqueda!")
            return redirect(request.META.get('HTTP_REFERER'))  # Redirige a la página anterior
        
        return render(request, 'store/search_product.html', {'searched': products})
    
    return redirect('home')  # Redirige a la página de inicio si la solicitud no es POST
