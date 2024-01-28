# Generated by Django 4.0 on 2024-01-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description_service', models.TextField(verbose_name='Descripción')),
                ('image_service', models.ImageField(blank=True, null=True, upload_to='services', verbose_name='Imagen')),
                ('datetime_creation', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('update_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha modificación')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['id'],
            },
        ),
    ]
