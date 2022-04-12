from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    """ All products """
    categories = None
    products = Product.objects.all()
    if request.GET:
        category = request.GET.get('category')
        categories = Category.objects.get(category_type=category)
        products = categories.product_category.all()

    context = {
        'products': products,
        'category': category
    }

    return render(request, 'products/product_list.html', context)
