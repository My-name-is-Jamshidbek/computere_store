# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from .views import CategoryListView # category_products, product_list_by_category, product_detail
                               
urlpatterns = [
    # path('category/<int:category_id>/', views.product_list_by_category, name='product_list_by_category'),
    path('category/<int:id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('add/', views.AddProductView, name='add_product'),
    path('add_category/', views.Add_CategoryView, name='add_category'),
    path('', views.CategoryListView.as_view(), name='category_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
