from .cart import Cart

# crear un procesador de contexto para que nuestro carrito pueda funcionar en todas las páginas del sitio.
def cart(request):
    # Devolver los datos predeterminados de nuestro Carrito
    return {'cart': Cart(request)}
