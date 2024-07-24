from django.shortcuts import render
from .forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    """Vista para iniciar sesión del usuario."""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Te has conectado con éxito.")
            return redirect('home')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.")
            return redirect('login') 
    else:
        return render(request, 'accounts/login.html', {})

def logout_user(request):
    """Vista para cerrar sesión del usuario."""
    logout(request)
    messages.success(request, "Te has desconectado exitosamente.")
    return redirect('home')

def register_user(request):
    """Vista para registrar un nuevo usuario."""
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Inicia sesión del usuario
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡¡Registro exitoso!! ¡Bienvenido!")
                return redirect('home')
        else:
            messages.error(request, "Hubo un problema al registrarte, por favor inténtalo de nuevo.")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', {'form': form})
