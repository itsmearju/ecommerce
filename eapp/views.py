from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . models import Category, Products

# Create your views here.


# def base(request): 
#     return render(request, 'base.html')


#----------------home page ----------#

def allProducts_page(request, cat_slug=None):
    cat_page = None
    products = None
    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        products = Products.objects.all().filter(category=cat_page, available=True)
    else:
        products = Products.objects.all().filter(available=True)
    return render(request, 'base.html', {'category':cat_page, 'products':products})
