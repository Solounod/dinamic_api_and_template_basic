from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Blog, CategoryBlog
from .serializers import BlogSerializer, BlogCategorySerializer
from .pagination import SmallSetPagination
# Create your views here.

class CategoryBlogList(ListAPIView):
    queryset = CategoryBlog.objects.all()
    serializer_class = BlogCategorySerializer
    pagination_class = SmallSetPagination

class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = SmallSetPagination

class BlogDetail(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
