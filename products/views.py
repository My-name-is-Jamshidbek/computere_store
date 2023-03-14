
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import ProductForm, CategoryForm
from django.views.generic import ListView, CreateView
# from .models import Product
from .models import Product, Category, Author, Category


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product/product_detail.html', {'product': product})


def product_detail_category(request, id, category_id):
    product = get_object_or_404(Product, id=id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'products/product/product_detail.html', {'product': product, 'category': category})


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


class ProductCreateView(CreateView):
    model = Product
    fields = ['brand', 'model', 'price', 'description', 'category', 'author', 'photo']
    template_name = 'products/product/add_product.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'products/product/product_list.html'
    context_object_name = 'products'

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].queryset = Category.objects.all()
    self.fields['author'].queryset = Author.objects.all()
