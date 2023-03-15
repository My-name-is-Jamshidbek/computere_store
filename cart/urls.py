"""
urls
"""
from django.urls import path
from .views import (
    cart_detail_view,
    add_to_cart_view,
    delete_cart_product_view,
)

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart_view, name='add_to_cart'),
    path('delete/<int:cart_product_id>/', delete_cart_product_view, name='delete_cart_product'),
]
