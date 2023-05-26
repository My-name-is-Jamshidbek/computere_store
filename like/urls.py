"""
urls
"""
from django.urls import path
from .views import (
    like_detail_view,
    add_to_like_view,
    delete_like_product_view
)

urlpatterns = [
    path('', like_detail_view, name='like_detail'),
    path('add/<int:product_id>/', add_to_like_view, name='add_to_like'),
    path('delete/<int:like_product_id>/', delete_like_product_view, name='delete_like_product'),
]
