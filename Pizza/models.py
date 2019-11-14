from django.db import models


# Create your models here.


class Pizza(models.Model):
    name = models.CharField(default='tested pizza',max_length=100)
    category = models.CharField(default='Pizza',max_length=100)
    preparing_time = models.CharField(default='10-15min',max_length=100)
    components = models.CharField(default='one two three four five',max_length=100)
    price = models.CharField(default='15$',max_length=100)

class Burger(models.Model):
    name = models.TextField(default='tested burger',max_length=100)
    category = models.TextField(default='Burger',max_length=100)
    preparing_time = models.TextField(default='10-15min',max_length=100)
    components = models.TextField(default='one two three four five',max_length=100)
    price = models.TextField(default='15$',max_length=100)

class Drink(models.Model):
    name = models.TextField(default='tested drink',max_length=100)
    category = models.TextField(default='Drink',max_length=100)
    preparing_time = models.TextField(default='10-15min',max_length=100)
    components = models.TextField(default='one two three four five',max_length=100)
    price = models.TextField(default='5$',max_length=100)

class Dessert(models.Model):
    name = models.TextField(default='tested dessert',max_length=100)
    category = models.TextField(default='Dessert',max_length=100)
    preparing_time = models.TextField(default='10-15min',max_length=100)
    components = models.TextField(default='one two three four five',max_length=100)
    price = models.TextField(default='20$',max_length=100)



