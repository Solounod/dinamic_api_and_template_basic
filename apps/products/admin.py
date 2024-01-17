from django.contrib import admin
from .models import Product, CategoryProduct, ImagesProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(ImagesProduct)