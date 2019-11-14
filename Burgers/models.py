from django.db import models
class Burger(models.Model):
    name = models.CharField(default='tested burger',max_length=100)
    category = models.CharField(default='Burger',max_length=100)
    preparing_time = models.CharField(default='10-15min',max_length=100)
    components = models.CharField(default='one two three four five',max_length=100)
    price = models.CharField(default='15$',max_length=100)
# Create your models here.
