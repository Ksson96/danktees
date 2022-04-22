from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category, Theme
from django.db.models import Q


def product_list(request, category_type):
    """ All products """
    category = None
    theme = ""
    search_query = None
    q = None

    if category_type == 'all':
        products = Product.objects.all()
        
    else:
        category = get_object_or_404(Category, category_type=category_type)
        products = category.product_category.all()

    if request.GET:
        if 'theme' in request.GET:
            theme = request.GET.get('theme')
            products = products.filter(theme__theme__contains=theme)

        if 'search' in request.GET:
            search_query = request.GET['search']
            query = Q(name__icontains=search_query) | Q(theme__theme__icontains=search_query)
            products = Product.objects.filter(query)

        if 'sortby' in request.GET:
            sort_query = request.GET['sortby']
            products = products.order_by(sort_query)

    context = {
        'products': products,
        'category': category,
        'theme': theme,
        'category_type': category_type,
        'search_query': search_query,
    }

    return render(request, 'products/product_list.html', context)


def product_details(request, pk):
    """ Single Product """
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        theme__theme__contains=product.theme.theme).exclude(
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