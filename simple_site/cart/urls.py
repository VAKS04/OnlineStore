from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('cart/',views.cart_func,name="cart"),
    path('cart_add/<slug:product_slug>',views.cart_add ,name="cart_add"),
    path('cart_change/<slug:product_slug>',views.cart_func ,name="cart_change"),
    path('cart_remove/<int:product_int>/',views.cart_remove ,name="cart_remove"),
]