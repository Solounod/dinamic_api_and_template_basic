from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product, CategoryProduct, ImagesProduct
from .serializers import ProductSerializer, CategoryProductSerializer, ImagesProductSerializer
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination
# Create your views here.

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = SmallSetPagination

class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryProductList(ListAPIView):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer

class ImagesProductList(ListAPIView):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductSerializer
    pagination_class = SmallSetPagination
