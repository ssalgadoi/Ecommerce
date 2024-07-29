from django import forms
from .models import ShippingAddress

# Formulario para la dirección de envío
class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo', 'max_length': 100})
    )
    shipping_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'max_length': 100})
    )
    shipping_address1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 1', 'max_length': 100})
    )
    shipping_address2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 2', 'max_length': 100}),
        required=False
    )
    shipping_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad', 'max_length': 100})
    )
    shipping_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado', 'max_length': 100}),
        required=False
    )
    shipping_zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal', 'max_length': 100}),
        required=False
    )
    shipping_country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País', 'max_length': 100})
    )

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']
        exclude = ['user']
