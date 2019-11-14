from django.contrib import admin

# Register your models here.
from .models import Pizza

admin.site.register(Pizza)

from .models import Burger

admin.site.register(Burger)

from .models import Dessert
admin.site.register(Dessert)

from .models import Drink
admin.site.register(Drink)