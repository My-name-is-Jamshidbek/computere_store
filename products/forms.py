from django import forms
from .models import Product
# forms.py
from django import forms
from .models import Product, Category, Author


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand', 'model', 'price', 'description', 'category', 'author', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
