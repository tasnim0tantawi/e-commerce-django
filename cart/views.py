from django.shortcuts import render
from . cart import Cart


# Create your views here.


def cart_summary(request):
    return render(request, 'cart/cart-summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))


def cart_delete(request):
    pass

def cart_update(request):
    pass
