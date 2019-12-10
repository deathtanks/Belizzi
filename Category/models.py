from django.db import models
from itertools import chain

class Product(models.Model):
    name = models.CharField(default='Product name', max_length=100)
    category = models.CharField(default='', max_length=100)
    preparing_time = models.CharField(default='10-15min', max_length=1000)
    components = models.CharField(default='one two three four five', max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    img = models.ImageField(upload_to='')

    def __str__(self):
        return self.name
