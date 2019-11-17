from django.contrib import admin
from .models import Burger, Dessert, Drink, Pizza

# Register your models here.
admin.site.register(Burger)
admin.site.register(Dessert)
admin.site.register(Drink)
admin.site.register(Pizza)
