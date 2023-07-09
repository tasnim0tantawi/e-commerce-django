from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
# we have to add this context processor to the settings.py file
# It makes the cart available in all templates and views of the project
