from django.db import models


# Create your models here.


class Pizza(models.Model):
    name = models.TextField(default='tested pizza')
    description = models.TextField(default='pizza descr')
    preparing_time = models.TextField(default='10-15min')
    components = models.TextField(default='one two three four five')
    price = models.TextField(default='15$')

class Burgers(models.Model):
    name = models.TextField(default='tested burger')
    description = models.TextField(default='burger descr')
    preparing_time = models.TextField(default='10-15min')
    components = models.TextField(default='one two three four five')
    price = models.TextField(default='15$')

class Drinks(models.Model):
    name = models.TextField(default='tested drink')
    description = models.TextField(default='drink descr')
    preparing_time = models.TextField(default='10-15min')
    components = models.TextField(default='one two three four five')
    price = models.TextField(default='5$')

class Desserts(models.Model):
        name = models.TextField(default='tested dessert')
        description = models.TextField(default='dessert descr')
        preparing_time = models.TextField(default='10-15min')
        components = models.TextField(default='one two three four five')
        price = models.TextField(default='20$')



