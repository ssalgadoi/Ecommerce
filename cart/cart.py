from store.models import Product
from accounts.models import Profile
import json

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Obtener solicitud
        self.request = request
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart 

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        # Tratar con el usuario que ha iniciado sesión
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            carty = str(self.cart)
            carty = carty.replace("\'" , "\"")
            current_user.update(old_cart=str(carty))

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total
        
        
        
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product_id, quantity):
        product_id = str(product_id)
        product_qty = int(quantity)
        self.cart[product_id] = product_qty
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            try:
                current_user = Profile.objects.get(user=self.request.user)
                carty = json.dumps(self.cart)  # Convierte el carrito a JSON
                current_user.old_cart = carty
                current_user.save()
            except Profile.DoesNotExist:
                # Manejar el caso en que el perfil no existe
                pass
        
        return self.cart

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
            
            if self.request.user.is_authenticated:
                try:
                    current_user = Profile.objects.get(user=self.request.user)
                    carty = json.dumps(self.cart)  # Convierte el carrito a JSON
                    current_user.old_cart = carty
                    current_user.save()
                except Profile.DoesNotExist:
                    # Manejar el caso en que el perfil no existe
                    pass

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        self.cart[product_id] = self.cart.get(product_id, 0) + product_qty
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            try:
                current_user = Profile.objects.get(user=self.request.user)
                carty = json.dumps(self.cart)  # Convierte el carrito a JSON
                current_user.old_cart = carty
                current_user.save()
            except Profile.DoesNotExist:
                # Manejar el caso en que el perfil no existe
                pass