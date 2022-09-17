# Generated by Django 3.2 on 2022-09-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_model',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electrónico [*]'),
        ),
        migrations.AlterField(
            model_name='customer_model',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre [*]'),
        ),
    ]