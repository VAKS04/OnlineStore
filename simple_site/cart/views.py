from django.shortcuts import render
from simple_app.models import Device
from .models import Cart
def cart_func(request):
    return render(request,"cart/cart_template.html")

def cart_add(request, product_slug):
    
    product = Device.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user = request.user, device = product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user = request.user,device = product)

    return render(request,"cart/cart_template.html")
# Create your views here.
