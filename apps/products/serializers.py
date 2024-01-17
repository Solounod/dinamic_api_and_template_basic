
from rest_framework import serializers
from .models import Product, CategoryProduct, ImagesProduct

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = '__all__'

class ImagesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryProductSerializer(read_only=True)
    images = ImagesProductSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = '__all__'