from django.urls import path
from .views import installment_list_view, installment_create_view, installment_update_view, installment_delete_view

urlpatterns = [
    path('', installment_list_view, name='installment_list'),
    path('new/', installment_create_view, name='installment_new'),
    path('<int:pk>/edit/', installment_update_view, name='installment_edit'),
    path('<int:pk>/delete/', installment_delete_view, name='installment_delete'),
]
