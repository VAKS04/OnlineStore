from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

# menu = [
#     {"title":"Главная","url_path":"index"},
#     {"title":"Авторизация","url_path":"other"},
#     ]
    
# catalog=[
#     {"title":"Смартфоны","url_path":"product"},
#     {"title":"Ноутбуки","url_path":"product"},
#     {"title":"Наушники","url_path":"product"},
#     ]


def index(request):
    return render(request,"simple_app/index.html")


def view_everyone_product(request,cat_slug):

    # filter_object = request.GET.get('')
    category = get_object_or_404(Category,slug=cat_slug)
    objects = Device.objects.filter(cat__slug=category.slug)
    name_model = [name.model for name in objects]
    return render(request,"simple_app/product.html",context={"product":objects,"name_product":name_model})

#Второй параметр является затычкой(возможно пока что)
def product(request,model_slug,cat_slug,prod_slug):
    post = get_object_or_404(Device,slug=prod_slug)
    return render(request,"simple_app/product_page.html",context={"product":post})


def other_func(request):
    return HttpResponse("<h2>Не главная")
# Create your views here.
