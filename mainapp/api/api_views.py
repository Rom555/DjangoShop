from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import CategorySerializer, CustomerSerializer, BaseProductSerializer
from ..models import Category, Customer, Product


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()
    lookup_field = 'id'


class CustomerListAPIView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProductPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class BaseProductAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = BaseProductSerializer
    pagination_class = ProductPagination
    queryset = Product.objects.all()
    lookup_field = 'id'
