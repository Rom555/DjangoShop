from django.urls import path

from .api_views import CategoryAPIView, CustomerListAPIView, BaseProductAPIView


urlpatterns = [
    path('categories', CategoryAPIView.as_view(), name='categories_list'),
    path('categories/<str:id>', CategoryAPIView.as_view(), name='categories_list'),
    path('customers', CustomerListAPIView.as_view(), name='customers_list'),
    path('products', BaseProductAPIView.as_view(), name='products_list'),
    path('products/<str:id>', BaseProductAPIView.as_view(), name='products_list')
]
