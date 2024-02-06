# Generated by Django 4.0 on 2024-02-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAbstract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('image_user', models.ImageField(blank=True, max_length=255, null=True, upload_to='users/', verbose_name='Imagen de usuario')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Último inicio de sesión')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['id'],
            },
        ),
    ]
