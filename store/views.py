from django.shortcuts import render
from .models import Category, Product

# Create your views here.


def store(request):
    all_products = Product.objects.all()
    context = {
        'all_products': all_products,
    }
    # in django, we have to reference by the key name in the context dictionary

    return render(request, 'store/store.html', context=context)


def categories(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories,
    }
    return context


