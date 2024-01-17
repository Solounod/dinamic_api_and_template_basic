from django.urls import path
from .views import ProductList, ProductDetail, CategoryProductList, ImagesProductList

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('category/', CategoryProductList.as_view(), name='category_product_list'),
    path('images/', ImagesProductList.as_view(), name='images_product_list'),
]
