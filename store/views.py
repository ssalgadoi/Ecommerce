from django.shortcuts import render, get_object_or_404, redirect 
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Te has conectado con exito.."))
            return redirect('home')
        else:
            messages.success(request, ("Existe un problema intentalo otra vez..."))
            return redirect('login') 
    else:   
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Te has desconectado..."))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("¡¡Registro exitoso!! ¡Bienvenido!"))
            return redirect('home')
        else:
            messages.success(request, ("Hubo un problema al registrarte, por favor inténtalo de nuevo.."))
            return redirect('register')
    else:  
        return render(request, 'register.html', {'form': form})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, foo):
    foo = foo.replace('-', ' ')
    categories = Category.objects.all()
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category, 'categories': categories})
    except Category.DoesNotExist:
        messages.success(request, ("Esta Categoria no existe!!"))
        return redirect('home')