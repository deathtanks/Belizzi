from django.shortcuts import render
from itertools import chain
from .models import Burger, Dessert, Drink, Pizza


# Create your views here.

def burger_view(request):
    return render(request, "burgers.html", {'burgers': Burger.objects.all()})

def dessert_view(request):
    return render(request, "desserts.html", {'desserts': Dessert.objects.all()})


def drink_view(request):
    return render(request, "drinks.html", {'drinks': Drink.objects.all()})


def pizza_view(request):
    return render(request, "pizzas.html", {'pizzas': Pizza.objects.all()})


def menu_view(request, *args, **kwargs):
    category = request.GET.get('category', 'all')
    if category == 'drinks':
        obj = {'items': Drink.objects.all()}
    elif category == 'pizzas':
        obj = {'items': Pizza.objects.all()}
    elif category == 'desserts':
        obj = {'items': Dessert.objects.all()}
    elif category == 'burgers':
        obj = {'items': Burger.objects.all()}

    else:
        obj = {'items': chain(Pizza.objects.all(),
                              Burger.objects.all(),
                              Drink.objects.all(),
                              Dessert.objects.all())}

    return render(request, "menu.html", obj)
