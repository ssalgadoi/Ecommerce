from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Modelo para los clientes
class Customer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Nombre del Cliente")
    last_name = models.CharField(max_length=30, verbose_name="Apellido del Cliente")
    phone = models.CharField(max_length=30, verbose_name="Teléfono del Cliente")
    email = models.EmailField(max_length=50, verbose_name="Email del Cliente")
    password = models.CharField(max_length=50, verbose_name="Contraseña del Cliente")
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

# Modelo para el perfil de usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

# Crear un perfil de usuario de forma predeterminada cuando el usuario se registra
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automatizar la creación del perfil
post_save.connect(create_profile, sender=User)