# Generated by Django 2.2.7 on 2019-12-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0005_auto_20191201_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='components',
            field=models.CharField(default='one two three four five', max_length=1000),
        ),
        migrations.AlterField(
            model_name='drink',
            name='preparing_time',
            field=models.CharField(default='10-15min', max_length=1000),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='components',
            field=models.CharField(default='one two three four five', max_length=1000),
        ),
    ]
