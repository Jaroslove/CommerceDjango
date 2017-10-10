from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import Product


class ProductDerailsView(DetailView):
    model = Product


def product_details_view_func(request, id):
    product_instance = Product.objects.get(id=id)
    template = 'products/product_details.html'
    context = {
        'object': product_instance
    }
    return render(request, template, context)
