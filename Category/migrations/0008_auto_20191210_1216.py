# Generated by Django 2.2.8 on 2019-12-10 12:16

from django.db import migrations

def move_products(apps, schema_editor):
    Burger = apps.get_model("Category", "Burger")
    Pizza = apps.get_model("Category", "Pizza")
    Dessert = apps.get_model("Category", "Dessert")
    Drink = apps.get_model("Category", "Drink")
    
    Product = apps.get_model("Category", "Product")
    copy_inner_data(Burger, Product)
    copy_inner_data(Pizza, Product)
    copy_inner_data(Dessert, Product)
    copy_inner_data(Drink, Product)
    
def copy_inner_data(from_model, to_model):
    for item in from_model.objects.all():
        product = to_model()
        product.name = item.name
        product.category = item.category
        product.preparing_time = item.preparing_time
        product.components = item.components
        product.price = item.price
        product.img = item.img
        
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0007_product'),
    ]

    operations = [
        
        migrations.RunPython(move_products),
    ]
