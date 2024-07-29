from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('subcategory/<str:foo>/', views.subcategory, name='subcategory'),
    path('subcategory/<str:foo>/', views.subcategory, name='subcategory'),
    path('search/', views.search, name='search'),
]