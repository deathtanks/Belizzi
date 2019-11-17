from django.shortcuts import render
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
