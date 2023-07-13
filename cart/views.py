from . cart import Cart
from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse


# Create your views here.


def cart_summary(request):
    return render(request, 'cart/cart-summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_quantity)
        response = JsonResponse({
            'Product name': product.title,
            'Product price': product.price,
            'Product quantity': product_quantity,
        })

        return response




def cart_delete(request):
    pass

def cart_update(request):
    pass
