from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
import calendar, datetime

from ckeditor.fields import RichTextField



#=======================================================================================================================================
# Page
#=======================================================================================================================================

class Page_Model(models.Model):
    name = models.CharField(max_length=250, default='sin_nombre', verbose_name='Nombre [*]')
    title = models.CharField(max_length=250, default='Sin título', verbose_name='Título [*]')
    subtitle = models.CharField(max_length=250, null=True, blank=True, verbose_name='Subtítulo')
    abstract = RichTextField(null=True, blank=True, verbose_name='Resumen')
    content = RichTextField(verbose_name='Contenido [*]')
    date = models.DateField(null=True, blank=True, verbose_name='Fecha')
    image_main = models.ImageField(null=True, blank=True, upload_to='img_page/', default='', verbose_name='Imagen principal')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['id']

    def __str__(self):
        return self.name
    
    

#=======================================================================================================================================
# Message
#=======================================================================================================================================

class Message_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre [*]')
    email = models.EmailField(max_length=250, verbose_name='Email [*]')
    subject = models.CharField(max_length=250, verbose_name='Asunto [*]')
    message = models.TextField(verbose_name='Mensaje [*]')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['id']

    def __str__(self):
        return self.subject



#=======================================================================================================================================
# Frontend_Search
#=======================================================================================================================================

class Frontend_Search_Model(models.Model):
    ''' Guarda las búsquedas del FrontEnd. '''
    name = models.CharField(max_length=250, verbose_name='Término de búsqueda [*]')
    created  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
        
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Búsqueda Frontend'
        verbose_name_plural = 'Búsquedas Frontend'
        ordering = ['id']

    def __str__(self):
        return self.name
    



#=======================================================================================================================================
# Backend_Search
#=======================================================================================================================================

class Backend_Search_Model(models.Model):
    ''' Guarda las búsquedas del Backend. '''
    name = models.CharField(max_length=250, verbose_name='Término de búsqueda [*]')
    created  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Búsqueda Backend'
        verbose_name_plural = 'Búsquedas Backend'
        ordering = ['id']

    def __str__(self):
        return self.name
