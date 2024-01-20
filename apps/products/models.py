from django.db import models
from .managers import ProductManager
from django.utils.text import slugify
# Create your models here.


class CategoryProduct(models.Model):

    class Meta:
        verbose_name = 'Categoria de productos'
        verbose_name_plural = 'Categorias de productos'
        ordering = ['id']

    categoryproduct = models.CharField(max_length=100, verbose_name='Categoria de productos')
    slug_category_product = models.SlugField(max_length=100, verbose_name='Slug', unique=True, blank=True)
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')

    def save(self, *args, **kwarg):
        if not self.slug_category_product:
            self.slug_category_product = slugify(self.categoryproduct)
        super().save(*args, **kwarg)

    def __str__(self):
        return f"{self.id}-{self.categoryproduct}"



class Product(models.Model):
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.PositiveIntegerField(verbose_name='Precio')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Imagen')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    objects = ProductManager()
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')

    def __str__(self):
        return f'{self.name} - ${self.price} - {self.category}'
    

class ImagesProduct(models.Model):
    class Meta:
        verbose_name = 'Imagen de producto'
        verbose_name_plural = 'Imagenes de productos'
        ordering = ['id']
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Imagen')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')
    
    def __str__(self):
        return f'{self.product} - {self.image}'