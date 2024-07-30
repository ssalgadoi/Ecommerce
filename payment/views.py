from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

# Create your views here.

def billing_info(request):
    if request.method == "POST":
        # Consigue el carrito
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()

        shipping_form = ShippingForm(request.POST)
        billing_form = PaymentForm(request.POST)
        # Crear sesión con información de envío
        
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping


        
        if shipping_form.is_valid() and billing_form.is_valid():
            # Aquí puedes guardar los datos del formulario o procesarlos como necesites
            return redirect('payment_checkout')  # O cualquier otra vista

        return render(request, "payment/billing_info.html", {
            'cart_products': cart_products,
            'quantities': quantities,
            'totals': totals,
            'shipping_form': shipping_form,
            'billing_form': billing_form
        })
    else:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()
        
        shipping_form = ShippingForm()
        billing_form = PaymentForm()

        return render(request, "payment/billing_info.html", {
            'cart_products': cart_products,
            'quantities': quantities,
            'totals': totals,
            'shipping_form': shipping_form,
            'billing_form': billing_form
        })

















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




def process_order(request):
    if request.POST:
        # Consigue el carrito
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()
        
        payment_form = PaymentForm(request.POST or None)
        # Obtener datos de sesión de envío
        my_shipping = request.session.get('my_shipping')
       
        
        # Recopilar información del pedido
        
        # Crear dirección de envío a partir de la información de la sesión
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}\n"
        amount_paid = totals
        
        # Crear un pedido
        if request.user.is_authenticated:
            # conectado
            user = request.user
            # Crear orden
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            
            messages.success(request, "Pedido realizado")
            return redirect('home')
        else:
            # Sin iniciar sesión
            create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            
            messages.success(request, "Pedido realizado")
            return redirect('home')

    else:
        messages.success(request, "Acceso denegado")
        return render('home')


