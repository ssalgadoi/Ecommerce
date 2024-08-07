from django.db import models
from datetime import datetime
from accounts.models import Customer

# Modelo para la categoría de productos
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre de la Categoría")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        

class Subcategory(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre de la Subcategoría")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'subcategoría'
        verbose_name_plural = 'subcategorías'

# Modelo para los países
class Country(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre del País")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'país'
        verbose_name_plural = 'países'
        
        
        
# Modelo para las marcas de productos
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la Marca")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'


# Modelo para los productos
class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre del Producto")
    description = models.CharField(max_length=250, verbose_name="Descripción del Producto")
    content = models.TextField(verbose_name="Contenido del Producto")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    image = models.ImageField(verbose_name="Imagen del Producto", upload_to="uploads/product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name="Subategoría")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Marca")
    origin = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="País Origen del Producto") 
    #Add sale Stuff
    is_sale = models.BooleanField(default=False, verbose_name="En Oferta")
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=12, verbose_name="Precio Oferta")
    
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

