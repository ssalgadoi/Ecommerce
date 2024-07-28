from django.shortcuts import render, redirect
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile


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
            return render(request, 'accounts/login.html')  # Renderiza la plantilla con mensaje de error
    return render(request, 'accounts/login.html')



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
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡¡Registro exitoso!! ¡Bienvenido!")
                return redirect('home')
        else:
            messages.error(request, "Hubo un problema al registrarte, por favor inténtalo de nuevo.")
    return render(request, 'accounts/register.html', {'form': form})


def update_user(request):
    """Vista para actualizar perfil usuario."""
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            
            login(request, current_user)
            messages.success(request, "El usuario ha sido actualizado !!")
            return redirect('home')
        return render(request, "accounts/update_user.html", {'user_form': user_form})
    else:
        messages.success(request, "Debes estar auntenticado para cambiar contraseña!!")  
        return redirect('home')     
    
    


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Su contraseña ha sido actualizada, inicie sesión nuevamente.")
                return redirect('login')
            else:
                # Manejo de errores del formulario
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)
        else:
            form = ChangePasswordForm(current_user)
        
        return render(request, "accounts/update_password.html", {'form': form})
    else:
        messages.error(request, "Debes iniciar sesión para ver esta página.")
        return redirect('home')


def update_info(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        if  form.is_valid():
            form.save()
            messages.success(request, "Tu información ha sido actualizada.")
            return redirect('home')
        return render(request, "accounts/update_info.html", {'form': form})
    else:
        messages.success(request, "Debes estar auntenticado para cambiar contraseña!!")  
        return redirect('home')  