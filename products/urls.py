# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductListView, name='product_list'),
    path('add/', views.AddProductView(), name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
