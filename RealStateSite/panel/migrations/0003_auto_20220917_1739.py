# Generated by Django 3.2 on 2022-09-17 20:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_page_model_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend_search_model',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Término de búsqueda [*]'),
        ),
        migrations.AlterField(
            model_name='frontend_search_model',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Término de búsqueda [*]'),
        ),
        migrations.AlterField(
            model_name='message_model',
            name='email',
            field=models.EmailField(max_length=250, verbose_name='Email [*]'),
        ),
        migrations.AlterField(
            model_name='message_model',
            name='message',
            field=models.TextField(verbose_name='Mensaje [*]'),
        ),
        migrations.AlterField(
            model_name='message_model',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nombre [*]'),
        ),
        migrations.AlterField(
            model_name='message_model',
            name='subject',
            field=models.CharField(max_length=250, verbose_name='Asunto [*]'),
        ),
        migrations.AlterField(
            model_name='page_model',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido [*]'),
        ),
        migrations.AlterField(
            model_name='page_model',
            name='name',
            field=models.CharField(default='sin_nombre', max_length=250, verbose_name='Nombre [*]'),
        ),
        migrations.AlterField(
            model_name='page_model',
            name='title',
            field=models.CharField(default='Sin título', max_length=250, verbose_name='Título [*]'),
        ),
    ]