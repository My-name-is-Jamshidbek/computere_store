from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', TemplateView.as_view(template_name='home.html'), name='profile'),
    path('logout/', TemplateView.as_view(template_name='home.html'), name='logout')
]
