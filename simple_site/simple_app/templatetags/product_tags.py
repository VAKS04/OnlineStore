from django.template import Library

from django.shortcuts import get_object_or_404
from simple_app.models import *
register = Library()

# @register.inclusion_tag("simple_app/card_product.html")
# def show_product():
#     product = Phone.objects.all()
#     return {"product":product}

@register.simple_tag()
def show_menu():
    menu = Menu.objects.all()
    return menu

@register.simple_tag()
def show_catalog():
    catalog = Category.objects.all()
    return catalog

@register.simple_tag()
def show_model(param):
    model_device = ModelDevice.objects.filter(cat__slug = param)
    return model_device