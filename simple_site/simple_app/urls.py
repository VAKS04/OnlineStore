from django.urls import path
from . import views

# app_name = "simple_app"

urlpatterns = [
    path('',views.index,name="index"),
    path('other/',views.other_func,name="other"),
    path('<slug:cat_slug>/',views.view_everyone_product,name="category"),
    path('<slug:cat_slug>/<slug:prod_slug>',views.product,name="product_page")
]
