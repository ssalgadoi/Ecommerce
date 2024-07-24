from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
]