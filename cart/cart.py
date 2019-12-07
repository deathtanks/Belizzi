from decimal import Decimal
from django.conf import settings
from Category.models import *

def get_prod_id(prod):
    return prod.category + "_" + str(prod.id)

def get_cat_from_prod_id(prod_id):
    return prod_id.split('_')[0]

def get_id_from_prod_id(prod_id):
    return prod_id.split('_')[1]

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        if get_prod_id(product) not in self.cart:
            self.cart[get_prod_id(product)] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[get_prod_id(product)]['quantity'] = quantity
        else:
            self.cart[get_prod_id(product)]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        if get_prod_id(product) in self.cart:
            del self.cart[get_prod_id(product)]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        #pdb.set_trace()

        for id in product_ids:
            manager = get_product(get_cat_from_prod_id(id))
            products = manager.objects.filter(id__in=get_id_from_prod_id(id))
            for product in products:
                self.cart[get_prod_id(product)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        