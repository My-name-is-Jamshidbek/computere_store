from products.models import Product, Category
from django.shortcuts import render

def HomePageView(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    context = {
        "category_list": category_list,
        "products_list": product_list
        }
    return render(request, template_name='home.html', context = context)