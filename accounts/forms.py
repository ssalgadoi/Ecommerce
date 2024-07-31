from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Dirección de correo'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.</small>'
            '</span>'
        )

        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Tu contraseña no puede ser muy similar a tu otra información personal.</li>'
            '<li>Tu contraseña debe contener al menos 8 caracteres.</li>'
            '<li>Tu contraseña no puede ser una contraseña comúnmente utilizada.</li>'
            '<li>Tu contraseña no puede ser completamente numérica.</li>'
            '</ul>'
        )

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>Introduce la misma contraseña de antes, para verificación.</small></span>'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Las direcciones de correo deben ser únicas.")
        return email

class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="",
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Dirección de correo'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.</small>'
            '</span>'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Las direcciones de correo deben ser únicas.")
        return email

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['new_password1', 'new_password2']:
            field = self.fields[field_name]
            field.widget.attrs['placeholder'] = 'Nueva Contraseña' if field_name == 'new_password1' else 'Confirmar nueva contraseña'
            field.label = ''
            field.help_text = (
                '<ul class="form-text text-muted small">'
                '<li>Tu contraseña no puede ser muy similar a tu otra información personal.</li>'
                '<li>Tu contraseña debe contener al menos 8 caracteres.</li>'
                '<li>Tu contraseña no puede ser una contraseña comúnmente utilizada.</li>'
                '<li>Tu contraseña no puede ser completamente numérica.</li>'
                '</ul>'
            ) if field_name == 'new_password1' else (
                '<span class="form-text text-muted"><small>Introduce la misma contraseña de antes, para verificación.</small></span>'
            )

class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'})
    )
    address1 = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 1'})
    )
    city = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'})
    )
    state = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'})
    )
    zipcode = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal'})
    )
    country = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'})
    )
    
    class Meta:
        model = Profile
        fields = ['phone', 'address1', 'city', 'state', 'zipcode', 'country']

            
class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'})
    )
    address1 = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección 1'})
    )

    city = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'})
    )
    state = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'})
    )
    zipcode = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal'})
    )
    country = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'})
    )
    
    class Meta:
        model = Profile
        fields = ['phone', 'address1', 'city', 'state', 'zipcode', 'country']
