from django.shortcuts import render


def shopping_cart(request):
    """ Shopping Cart View """

    return render(request, 'cart.html', {})


def checkout(request):
    """ Checkout View """

    return render(request, 'checkout.html', {})