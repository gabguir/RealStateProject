from django.db import models
from django.utils import timezone
import calendar, datetime

#=======================================================================================================================================
# Modelos:
# Property
# Agent
# Customer
# Page
# Article
# Category
# Image
#=======================================================================================================================================

class Property(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    price = models.IntegerField(verbose_name='Precio')
    location = models.CharField(max_length=50, verbose_name='Localización')
    # status = boolean(TRUE)
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos '''
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'
        ordering = ['id']

    def __str__(self):
        return self.address + " " + self.location

class Agent(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=254, verbose_name='Correo electrónico')
    image = models.ImageField(null=True, blank=True, upload_to='agent/', default='', verbose_name='Imagen')
    description = models.TextField(null=True, blank=True, default='', verbose_name='Descripción')
    url_twitter = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Twitter')
    url_facebook = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Facebook')
    url_linkedin = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Linkedin')
    url_instagram = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Instagram')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos '''
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        ordering = ['id']
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=254, verbose_name='Correo electrónico')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos '''
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.name



#=======================================================================================================================================
# Modelos para blog
#=======================================================================================================================================

class Page(models.Model):
    name = models.CharField(max_length=250, default='Sin nombre', verbose_name='Nombre')
    title = models.CharField(max_length=250, default='Sin título', verbose_name='Título')
    subtitle = models.CharField(max_length=250, null=True, blank=True, verbose_name='Subtítulo')
    abstract = models.TextField(null=True, blank=True, verbose_name='Resumen')

    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha')
    content = models.TextField(verbose_name='Contenido')
    #draft = models.BooleanField(null=True, blank=True, default=True, verbose_name='Borrador')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['id']

    def __str__(self):
        return self.name



class Article(models.Model):
    name = models.CharField(max_length=250, default='Sin nombre', verbose_name='Nombre')
    title = models.CharField(max_length=250, default='Sin título', verbose_name='Título')
    subtitle = models.CharField(max_length=250, null=True, blank=True, verbose_name='Subtítulo')
    abstract = models.TextField(null=True, blank=True, verbose_name='Resumen')
    date = models.DateField(null=True, blank=True, verbose_name='Fecha')
    content = models.TextField(null=True, blank=True, verbose_name='Contenido')
    image = models.ImageField(null=True, blank=True, upload_to='article/', default='', verbose_name='Imagen')
    draft = models.BooleanField(null=True, blank=True, default=True, verbose_name='Borrador')
    fk_categoria = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoría') 
    #fk_autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Autor') 

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True, default='', verbose_name='Descripción')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

    def __str__(self):
        return self.name
    
    
    
class Image(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    pic = models.ImageField(null=True, blank=True, upload_to='image/', default='', verbose_name='Imagen')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de publicación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        ordering = ['id']

    def __str__(self):
        return self.name
    
    
