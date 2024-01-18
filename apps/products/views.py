from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product, CategoryProduct, ImagesProduct
from .serializers import ProductSerializer, CategoryProductSerializer, ImagesProductSerializer
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination
# Create your views here.


class CategoryProductList(ListAPIView):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer

class ProductList(ListAPIView):
    
    serializer_class = ProductSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        category = self.kwargs['list_products']
        list_products = Product.objects.filter(category__slug_category_product=category)
        return list_products
        

class ProductDetail(RetrieveAPIView):
    
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    queryset = Product.objects.filter()



class ImagesProductList(ListAPIView):
    
    serializer_class = ImagesProductSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        product = self.kwargs['id']
        list_images = ImagesProduct.objects.filter(product__id=product)
        return list_images
