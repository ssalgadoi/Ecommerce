from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo', 'maxlength': '100'}),
        required=True
    )
    shipping_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'maxlength': '100'}),
        required=True
    )
    shipping_address1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 1', 'maxlength': '100'}),
        required=True
    )
    shipping_address2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 2', 'maxlength': '100'}),
        required=False
    )
    shipping_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad', 'maxlength': '100'}),
        required=True
    )
    shipping_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado', 'maxlength': '100'}),
        required=False
    )
    shipping_zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal', 'maxlength': '10'}),
        required=False
    )
    shipping_country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País', 'maxlength': '100'}),
        required=True
    )

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']
        exclude = ['user']


from django import forms



class PaymentForm(forms.Form):
    card_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo', 'maxlength': '100'}),
        required=True
    )
    card_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de tarjeta', 'maxlength': '19'}),
        required=True
    )
    card_exp_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de expiración (MM/AA)', 'maxlength': '7'}),
        required=True
    )
    card_cvv_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV', 'maxlength': '4'}),
        required=True
    )
    card_address1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 1', 'maxlength': '100'}),
        required=True
    )
    card_address2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 2', 'maxlength': '100'}),
        required=False
    )
    card_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad', 'maxlength': '100'}),
        required=True
    )
    card_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado', 'maxlength': '100'}),
        required=False
    )
    card_zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal', 'maxlength': '10'}),
        required=True
    )
    card_country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País', 'maxlength': '100'}),
        required=True
    )
