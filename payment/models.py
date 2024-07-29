from django.db import models
from django.contrib.auth.models import User

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
