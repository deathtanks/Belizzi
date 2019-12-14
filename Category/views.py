from django.shortcuts import render
from itertools import chain
from .models import Product


def menu_view(request, *args, **kwargs):
    category = request.GET.get('category', 'all')

    if category == 'drinks':
        obj = {'items': Product.objects.filter(category="Drink")}
    elif category == 'pizzas':
        obj = {'items': Product.objects.filter(category="Pizza")}
    elif category == 'desserts':
        obj = {'items': Product.objects.filter(category="Dessert")}
    elif category == 'burgers':
        obj = {'items': Product.objects.filter(category="Burger")}

    else:
        obj = {'items': Product.objects.all()}

    return render(request, "menu.html", obj)
