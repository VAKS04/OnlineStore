from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('<slug:cat_slug>/',views.view_everyone_product,name="category"),
    path('<slug:cat_slug>/<slug:model_slug>/<slug:prod_slug>',views.product,name="product_page")
]
