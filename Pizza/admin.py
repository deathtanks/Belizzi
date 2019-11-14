from django.contrib import admin

# Register your models here.
from .models import Pizza

admin.site.register(Pizza)

from .models import Burgers

admin.site.register(Burgers)

from .models import Desserts
admin.site.register(Desserts)

from .models import Drinks
admin.site.register(Drinks)