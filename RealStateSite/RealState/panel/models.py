from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    ''' Guarda las búsquedas '''
    name = models.CharField(max_length=250, verbose_name='Término de búsqueda')
    created  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Usuario')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Búsqueda'
        verbose_name_plural = 'Búsquedas'
        ordering = ['id']

    def __str__(self):
        return self.name