from rest_framework import serializers
from .models import Blog, CategoryBlog

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryBlog
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
