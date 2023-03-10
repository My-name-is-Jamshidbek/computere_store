
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CategoryForm
from django.views.generic import ListView
# from .models import Product
from .models import Product, Category, Author, Category


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product/product_detail.html', {'product': product})


def product_detail_category(request, id, category_id):
    product = get_object_or_404(Product, id=id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'products/product/product_detail.html', {'product': product, 'category': category})

#
#
# def product_list_by_category(request, slug):
#     category = get_object_or_404(Category, name=slug)
#     products = Product.objects.filter(category=category)
#     return render(request, 'store/product/list.html', {'category': category, 'products': products})
#

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.product_set.all()
    return render(request, 'products/category/category_products.html', {'category': category, 'products': products})


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category/category_list.html'
    context_object_name = 'categories'


def Add_CategoryView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category/add_category.html', {'form': form})

def AddProductView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product/add_product.html', {'form': form})


class ProductListView(ListView):
    model = Product
    template_name = 'products/product/product_list.html'
    context_object_name = 'products'

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].queryset = Category.objects.all()
    self.fields['author'].queryset = Author.objects.all()
