from .cart import Cart


def cart_number(request):
    return {'cart_num':Cart(request)}