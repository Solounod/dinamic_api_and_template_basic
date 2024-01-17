from django.db import models

# Create your models here.
class LinkSocial(models.Model):
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200)
    img = models.ImageField(upload_to='media/contact/', verbose_name="Icono link")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name= "Enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    email = models.EmailField(verbose_name="Correo electrónico", max_length=100)
    phone_number = models.CharField(verbose_name="Número de teléfono", max_length=50)
    subject = models.CharField(verbose_name="Asunto", max_length=200)
    message = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name= "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['name']

    def __str__(self):
        return self.name