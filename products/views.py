
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import ProductForm, CategoryForm
from django.views.generic import ListView, CreateView
# from .models import Product
from .models import Product, Category, Author, Category, Photo


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    product_ = Product.objects.get(id=product.pk)
    photos = Photo.objects.filter(product=product_)
    return render(request, 'products/product/product_detail.html', {'product': product, 'photos': photos})


def product_detail_category(request, id, category_id):
    product = get_object_or_404(Product, id=id)
    category = get_object_or_404(Category, id=category_id)
    photos = Photo.objects.filter(product=product)
    return render(request, 'products/product/product_detail.html', {'product': product, 'category': category, 'photos': photos})


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



def ProductCreate(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        photos = request.FILES.getlist('photos')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')
        category = Category.objects.get(id=category_id)
        author = Author.objects.get(id=author_id)
        product = Product(brand=brand, model=model, price=price, description=description, image=image, category=category, author=author)
        product.save()

        product_ = Product.objects.get(id=product.pk)

        # Add any uploaded photos to the new Product object
        if photos:
            print(photos)
            for photo in photos:
                print(photo)
                new_photo = Photo(image=photo, product=product_)
                new_photo.save()

        return redirect('product_detail', id=product.pk)
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'categories': categories,
        'authors': authors
    }
    # Render the form for creating a new product
    return render(request, 'products/product/add_product.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'products/product/product_list.html'
    context_object_name = 'products'

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['category'].queryset = Category.objects.all()
    self.fields['author'].queryset = Author.objects.all()
