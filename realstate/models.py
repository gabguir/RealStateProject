from django.db import models
# from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from agent.models import Agent_Model

#=======================================================================================================================================
# Realstate
#=======================================================================================================================================

class Realstate_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre [*]')
    address = models.CharField(max_length=250, verbose_name='Dirección [*]')
    price = models.IntegerField(verbose_name='Precio [*]')
    location = models.CharField(max_length=250, verbose_name='Localización [*]')
    fk_tipo_inmueble = models.ForeignKey('Realstate_Type_Model', on_delete=models.DO_NOTHING, verbose_name='Tipo de inmueble [*]') 
    fk_agent = models.ForeignKey('agent.Agent_Model', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Agente') 
    
    bath_qty = models.CharField(max_length=2, verbose_name='Cantidad de baños [*]')
    room_qty = models.CharField(max_length=2, verbose_name='Cantidad de habitaciones [*]')
    date = models.DateField(verbose_name='Fecha')
    description = RichTextField(null=True, blank=True, verbose_name='Descripción')
    # status = boolean(TRUE)
    
    image_main = models.ImageField(null=True, blank=True, upload_to='img_realstate/', default='', verbose_name='Imagen principal')
    image_01 = models.ImageField(null=True, blank=True, upload_to='img_realstate/', default='', verbose_name='Imagen carrusel 01')
    image_02 = models.ImageField(null=True, blank=True, upload_to='img_realstate/', default='', verbose_name='Imagen carrusel 02')
    image_03 = models.ImageField(null=True, blank=True, upload_to='img_realstate/', default='', verbose_name='Imagen carrusel 03')
    image_04 = models.ImageField(null=True, blank=True, upload_to='img_realstate/', default='', verbose_name='Imagen carrusel 04')
    image_05 = models.ImageField(null=True, blank=True, upload_to='img_realstate/', default='', verbose_name='Imagen carrusel 05')
    
    draft = models.BooleanField(null=True, blank=True, default=True, verbose_name='Borrador')
    # user
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos '''
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'
        ordering = ['-date']

    def __str__(self):
        return self.address + " " + self.location


#=======================================================================================================================================
# Realstate_Type
#=======================================================================================================================================

class Realstate_Type_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre [*]')
    description = RichTextField(null=True, blank=True, default='', verbose_name='Descripción')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Tipo de inmueble'
        verbose_name_plural = 'Tipos de inmueble'
        ordering = ['-id']

    def __str__(self):
        return self.name
    
    

#=======================================================================================================================================
# Message_Realstate
#=======================================================================================================================================

class Message_Realstate_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre [*]')
    email = models.EmailField(max_length=250, verbose_name='Email [*]')
    subject = models.CharField(max_length=250, verbose_name='Asunto [*]')
    message = models.TextField(verbose_name='Mensaje [*]')
    fk_realstate = models.ForeignKey('Realstate_Model', on_delete=models.DO_NOTHING, verbose_name='Inmueble [*]') 
    fk_agent = models.ForeignKey('agent.Agent_Model', on_delete=models.DO_NOTHING, verbose_name='Agente [*]') 
    
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Mensaje desde inmueble'
        verbose_name_plural = 'Mensajes desde inmuebles'
        ordering = ['-created']

    def __str__(self):
        return self.subject
