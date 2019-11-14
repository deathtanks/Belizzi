from django.db import models
class Drink(models.Model):
    name = models.CharField(default='tested drink',max_length=100)
    category = models.CharField(default='Drink',max_length=100)
    preparing_time = models.CharField(default='10-15min',max_length=100)
    components = models.CharField(default='one two three four five',max_length=100)
    price = models.CharField(default='5$',max_length=100)
# Create your models here.
