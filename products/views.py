
from django.shortcuts import render, redirect
from .forms import ProductForm, CategoryForm
from django.views.generic import ListView
from .models import Product
from .models import Product, Category, Author


# views.py
def Add_CategoryView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def AddProductView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].queryset = Category.objects.all()
    self.fields['author'].queryset = Author.objects.all()
