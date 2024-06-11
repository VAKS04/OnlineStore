from django.template import Library
from cart.models import *

register = Library()

@register.simple_tag()
def tag_of_cart(request):
    cart = Cart.objects.filter(user=request.user)
    return cart