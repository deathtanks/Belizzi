from django.db import models


# Create your models here.


class Pizza(models.Model):
    name = models.CharField(default='tested pizza',max_length=100)
    category = models.CharField(default='Pizza',max_length=100)
    preparing_time = models.CharField(default='10-15min',max_length=100)
    components = models.CharField(default='one two three four five',max_length=100)
    price = models.DecimalField(...,max_digits=5,decimal_places=2)








