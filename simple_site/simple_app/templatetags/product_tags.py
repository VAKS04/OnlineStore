from django.template import Library

from django.shortcuts import get_object_or_404
from simple_app.models import *
register = Library()

@register.inclusion_tag("simple_app/catalog_panel.html")
def show_catalog_panel():
    catalog = Category.objects.all()
    return {"catalog":catalog}

@register.simple_tag()
def show_menu():
    menu = Menu.objects.all()
    return menu

@register.simple_tag()
def show_model(param):
    model_device = ModelDevice.objects.filter(cat__slug = param)
    return model_device