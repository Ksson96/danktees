from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    """ All products """
    products = Product.objects.all()
    category = None
    
    if request.GET:
        category = request.GET.get('category')
        categories = get_object_or_404(Category, category_type=category)
        products = categories.product_category.all()


    # if request.GET:
    #     category = request.GET.get('category')
    #     categories = Category.objects.get(category_type=category)
    #     products = categories.product_category.all()

    context = {
        'products': products,
        'category': category
    }

    return render(request, 'products/product_list.html', context)


def product_details(request, pk):
    """ Single Product """
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        category__name__contains=product.category.name).exclude(
            pk=product.pk)
    
    sizes = product.size.all()
    if len(sizes) == 0:
        sizes = None

    context = {
        'product': product,
        'sizes': sizes,
        'related_products': related_products,
    }

    return render(request, 'products/product_details.html', context)