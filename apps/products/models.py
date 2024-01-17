from django.db import models

# Create your models here.


class CategoryProduct(models.Model):

    class Meta:
        verbose_name = 'Categoria de productos'
        verbose_name_plural = 'Categorias de productos'
        ordering = ['id']

    categoryproduct = models.CharField(max_length=100, verbose_name='Categoria de productos')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')

    def __str__(self):
        return f"{self.id}-{self.category_workshop}"



class Product(models.Model):
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.IntegerField(max_digits=10, verbose_name='Precio')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Imagen')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
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