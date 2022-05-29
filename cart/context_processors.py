from .models import Cart,CartItem
from .views import _cart_id

def counter(request):
    cart_counter = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id= _cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_counter+=cart_item.quantity
            
        except Cart.DoesNotExist:
            cart_counter=0
    
    print(cart_counter)
    print(cart_items)
        
    return dict(cart_counter=cart_counter)