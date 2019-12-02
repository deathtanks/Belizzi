from django.db import models


# Create your models here.


class Pizza(models.Model):
    name = models.CharField(default='tested pizza', max_length=100)
    category = models.CharField(default='Pizza', max_length=100)
    preparing_time = models.CharField(default='10-15min', max_length=100)
    components = models.CharField(default='one two three four five', max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.ImageField(upload_to='Pizza')

    def __str__(self):
        return self.name


class Burger(models.Model):
    name = models.CharField(default='tested burger', max_length=100)
    category = models.CharField(default='Burger', max_length=100)
    preparing_time = models.CharField(default='10-15min', max_length=100)
    components = models.CharField(default='one two three four five', max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.ImageField(upload_to='Burgers')

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(default='tested dessert', max_length=100)
    category = models.CharField(default='Dessert', max_length=100)
    preparing_time = models.CharField(default='10-15min', max_length=100)
    components = models.CharField(default='one two three four five', max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.ImageField(upload_to='Desserts')

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(default='tested drink', max_length=100)
    category = models.CharField(default='Drink', max_length=100)
    preparing_time = models.CharField(default='10-15min', max_length=1000)
    components = models.CharField(default='one two three four five', max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.ImageField(upload_to='Drink')

    def __str__(self):
        return self.name


