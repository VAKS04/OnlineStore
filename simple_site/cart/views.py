from django.shortcuts import render


def cart_func(request):
    return render(request,"cart/cart_template.html")
# Create your views here.
