from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
     
     def _create_user(self, username, email, first_name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
     
     def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,           
            is_superuser = False,
            is_staff = False,
            **extra_fields)
    
     def create_superuser(self,username, email, first_name, last_name, password=None,**extra_fields):
        return self._create_user(
            username = username,
            email = self.normalize_email(email),
            last_name = last_name,
            first_name = first_name,
            password = password,
            is_superuser = True,
            is_staff = True,
            **extra_fields)
        
        

class UserAbstract(AbstractUser):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

    email = models.EmailField(
        unique=True, 
        verbose_name='Correo electrónico')
    username = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name='Nombre de usuario')
    password = models.CharField(
        max_length=100, 
        verbose_name='Contraseña')
    image_user = models.ImageField(
        upload_to='users/',
        max_length=255, 
        verbose_name='Imagen de usuario', 
        blank=True, 
        null=True)
    first_name = models.CharField(
        max_length=100, 
        verbose_name='Nombre',
        blank=True,
        null=True)
    last_name = models.CharField(
        max_length=100, 
        verbose_name='Apellido',
        blank=True,
        null=True)
    is_active = models.BooleanField(
        default=True, 
        verbose_name='Activo')
    is_staff = models.BooleanField(
        default=False, 
        verbose_name='Staff')
    date_joined = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creación')
    last_login = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Último inicio de sesión')
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.id}-{self.username}"
    

   