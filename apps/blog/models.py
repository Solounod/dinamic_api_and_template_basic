from django.db import models

# Create your models here.

class CategoryBlog(models.Model):
    class Meta:
        verbose_name = 'Categoria de blog'
        verbose_name_plural = 'Categorias de blog'
        ordering = ['id']

    category_blog = models.CharField(max_length=100, verbose_name='Categoria de blog')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')

    def __str__(self):
        return f"{self.id}-{self.category_blog}"
    

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['id']

    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE, verbose_name='Categoria')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    header = models.CharField(max_length=200, verbose_name='Encabezado')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name='Imagen')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')

    def __str__(self):
        return f'{self.title} - {self.category}'