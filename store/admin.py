from django.contrib import admin 
from .models import Category, Product, Order, Brand, Country, Subcategory

admin.site.register(Category)

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Country)
admin.site.register(Subcategory)