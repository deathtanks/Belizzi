from django.db import models
class Dessert(models.Model):
    name = models.CharField(default='tested dessert',max_length=100)
    category = models.CharField(default='Dessert',max_length=100)
    preparing_time = models.CharField(default='10-15min',max_length=100)
    components = models.CharField(default='one two three four five',max_length=100)
    price = models.DecimalField(..., max_digits=5, decimal_places=2)

# Create your models here.
