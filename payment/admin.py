from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)


# Crear un artículo de pedido en línea

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    
# Ampliar nuestro modelo de pedido

class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    fields = ["user", "full_name", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]
    inlines = [OrderItemInline]

# Modelo de orden de baja
admin.site.unregister(Order)

# Vuelva a registrar nuestro pedido y artículos de pedido

admin.site.register(Order, OrderAdmin)