from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Modelo para la dirección de envío del usuario
class ShippingAddress(models.Model):
    # ForeignKey debe estar bien escrito
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=100 )
    shipping_email = models.CharField(max_length=100 )
    shipping_address1 = models.CharField(max_length=100 )
    shipping_address2 = models.CharField(max_length=100 )
    shipping_city = models.CharField(max_length=100 )
    shipping_state = models.CharField(max_length=100,null=True, blank=True )
    shipping_zipcode = models.CharField(max_length=100,null=True, blank=True )
    shipping_country = models.CharField(max_length=100 )

    # Metadatos del modelo
    class Meta:
        verbose_name_plural = "Dirección de Envíos"

    # Método para retornar una representación legible del objeto
    def __str__(self):
        return f'Dirección de Envíos - {str(self.id)}'

# Modelo para los pedidos
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(max_length=254, verbose_name="Correo")
    shipping_address = models.CharField(max_length=100, default='', blank=True, verbose_name="Dirección")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad pagada")
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del pedido")

    def __str__(self):
        return f'Orden - {str(self.id)}'
    
    class Meta:
        verbose_name = 'orden'
        verbose_name_plural = 'órdenes'

# Modelo para los artículos del pedido
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Item de Orden - {str(self.id)}'
