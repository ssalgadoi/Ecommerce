from django.contrib import admin
from .models import Customer, Profile
from django.contrib.auth.models import User

# Registrar modelos en el administrador
admin.site.register(Customer)
admin.site.register(Profile)

# Mezclar información de perfil e información de usuario
class ProfileInline(admin.StackedInline):
    model = Profile

# Ampliar modelo de usuario
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

# Re-registrar el UserAdmin para incluir el ProfileInline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
