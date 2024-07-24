from django.shortcuts import render
from store.models import Product, Category

# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'base/home.html', {'products': products, 'categories': categories})
