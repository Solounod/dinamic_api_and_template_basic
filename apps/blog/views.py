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
    
    serializer_class = BlogSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        category = self.kwargs['id']
        list_blogs = Blog.objects.filter(category__id=category)
        return list_blogs

class BlogDetail(RetrieveAPIView):
    
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    queryset = Blog.objects.filter()
