# Generated by Django 3.2 on 2022-09-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0006_realstate_model_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realstate_model',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Dirección [*]'),
        ),
        migrations.AlterField(
            model_name='realstate_model',
            name='bath_qty',
            field=models.CharField(max_length=2, verbose_name='Cantidad de baños [*]'),
        ),
        migrations.AlterField(
            model_name='realstate_model',
            name='location',
            field=models.CharField(max_length=250, verbose_name='Localización [*]'),
        ),
        migrations.AlterField(
            model_name='realstate_model',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nombre [*]'),
        ),
        migrations.AlterField(
            model_name='realstate_model',
            name='room_qty',
            field=models.CharField(max_length=2, verbose_name='Cantidad de habitaciones [*]'),
        ),
    ]