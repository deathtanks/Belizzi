from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    #pdb.set_trace() 
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                #pdb.set_trace()
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'checkout_done.html', {'cart': cart,'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'checkout.html', {'cart': cart,'form': form})


def all_orders(request):

    orders = []
    for order in Order.objects.all():
        item = {}
        item["id"] = order.id
        item["table"] = order.table
        item["created"] = order.created
        item["items"] = OrderItem.objects.filter(order = order)
        orders.append(item)


    return render(request, 'orders.html', {'orders': orders})

