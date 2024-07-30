from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress

# Create your views here.
def payment_checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # Obtén o crea una instancia de ShippingAddress para el usuario autenticado
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)

        # Inicializa el formulario con la instancia obtenida o creada
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    else:
        # Inicializa el formulario para usuarios no autenticados
        shipping_form = ShippingForm(request.POST or None)

    if request.method == 'POST':
        if shipping_form.is_valid():
            shipping_form.save()
            # Aquí puedes manejar la lógica adicional después de guardar el formulario, como redirigir al éxito del pago
            return redirect('payment_success')

    return render(request, "payment/payment_checkout.html", {
        'cart_products': cart_products,
        'quantities': quantities,
        'totals': totals,
        'shipping_form': shipping_form
    })

def payment_success(request):
    return render(request, "payment/payment_success.html", {})