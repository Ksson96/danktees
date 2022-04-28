from django.shortcuts import render


def view_cart(request):

    return render(request, 'store/cart.html')