from django.urls import path
from . import views

urlpatterns = [
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_checkout/', views.payment_checkout, name='payment_checkout'),

]