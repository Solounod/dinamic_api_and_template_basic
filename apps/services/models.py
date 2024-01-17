from django.db import models

# Create your models here.
class Services(models.Model):
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['id']

    name_service = models.CharField(max_length=100, verbose_name='Nombre')
    description_service = models.TextField(verbose_name='Descripción')
    image_service = models.ImageField(upload_to='services', null=True, blank=True, verbose_name='Imagen')
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha creación')
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha modificación')

    def __str__(self):
        return f'{self.name}'