from django.urls import path
from .views import ProductList, ProductDetail, CategoryProductList, ImagesProductList

urlpatterns = [
    
    
    path('category/', CategoryProductList.as_view(), name='category_product_list'),
    path('category/<str:list_products>/', ProductList.as_view(), name='product_list'),
    path('category/productdetail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('images/<int:id>', ImagesProductList.as_view(), name='images_product_list'),
]
