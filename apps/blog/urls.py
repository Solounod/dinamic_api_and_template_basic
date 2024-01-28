from django.urls import path
from .views import CategoryBlogList, BlogDetail, BlogList

urlpatterns = [
    path('categoryblog/', 
        CategoryBlogList.as_view(), 
        name='category_blog_list'),
    path('categoryblog/<int:id>/', 
        BlogList.as_view(), 
        name='blog_list'),
    path('categoryblog/blogdetail/<str:slug>/', 
        BlogDetail.as_view(),
        name='blog_detail'),
]
