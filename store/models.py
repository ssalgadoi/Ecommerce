from django.db import models
from datetime import datetime

# Modelo para la categoría de productos
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre de la Categoria")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

# Modelo para las marcas de productos
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la Marca")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

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

# Modelo para los productos
class Product(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código del Producto")  # Nuevo campo código
    name = models.CharField(max_length=30, verbose_name="Nombre del Producto")
    description = models.CharField(max_length=250, verbose_name="Descripcion del Producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del producto")
    image = models.ImageField(verbose_name="Imagen del Producto", upload_to="uploads/product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Marca")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")  # Nuevo campo disponible
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

# Modelo para los pedidos
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Cliente")
    quantity = models.IntegerField(default=1, verbose_name="Cantidad")
    address = models.CharField(max_length=100, default='', blank=True, verbose_name="Dirección")
    phone = models.CharField(max_length=20, default='', blank=True, verbose_name="Teléfono")
    date = models.DateField(default=datetime.today, verbose_name="Fecha")
    status = models.BooleanField(default=False, verbose_name="Estado")
    
    def __str__(self):
        return str(self.product)
    
    class Meta:
        verbose_name = 'orden'
        verbose_name_plural = 'ordenes'
