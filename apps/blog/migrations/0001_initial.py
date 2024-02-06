# Generated by Django 4.0 on 2024-02-05 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_blog', models.CharField(max_length=100, verbose_name='Categoria de blog')),
                ('datetime_creation', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('update_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha modificación')),
            ],
            options={
                'verbose_name': 'Categoria de blog',
                'verbose_name_plural': 'Categorias de blog',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('header', models.CharField(max_length=200, verbose_name='Encabezado')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen')),
                ('datetime_creation', models.DateTimeField(auto_now=True, verbose_name='Fecha creación')),
                ('update_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha modificación')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoryblog', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['id'],
            },
        ),
    ]
