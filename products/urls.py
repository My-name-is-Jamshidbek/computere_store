# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from .views import CategoryListView # category_products, product_list_by_category, product_detail
                               
urlpatterns = [
    # product
    path('add/', views.ProductCreate, name='add_product'),
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),

    # categories
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('category/add_category/', views.Add_CategoryView, name='add_category'),
    path('category/<int:category_id>/<int:id>/', views.product_detail_category, name='product_detail_category'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
