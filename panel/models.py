from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
import calendar, datetime

from ckeditor.fields import RichTextField
from agent.models import Agent_Model


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
    draft = models.BooleanField(null=True, blank=True, default=True, verbose_name='Borrador')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['-date']

    def __str__(self):
        return self.name
    
    

#=======================================================================================================================================
# Message_Contact
#=======================================================================================================================================

class Message_Contact_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre [*]')
    email = models.EmailField(max_length=250, verbose_name='Email [*]')
    subject = models.CharField(max_length=250, verbose_name='Asunto [*]')
    message = models.TextField(verbose_name='Mensaje [*]')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Mensaje Form Contacto'
        verbose_name_plural = 'Mensajes Form Contacto'
        ordering = ['-created']

    def __str__(self):
        return self.subject




#=======================================================================================================================================
# Message_Agent
#=======================================================================================================================================

class Message_Agent_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Asunto [*]')
    message = models.TextField(verbose_name='Mensaje [*]')
    #agent_sender = models.CharField(max_length=250, verbose_name='Nombre [*]')
    agent_sender = models.IntegerField(verbose_name='Remitente [*]')
    #agent_sender = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Remitente [*]')
    agent_receiver = models.ForeignKey('agent.Agent_Model', on_delete=models.DO_NOTHING, verbose_name='Destinatario [*]') 
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Mensaje de Agente'
        verbose_name_plural = 'Mensajes de Agentes'
        ordering = ['-created']

    def __str__(self):
        # return self.name
        return f'{self.name} - REC: {self.agent_receiver} - SEND: {self.agent_sender}'



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
        ordering = ['-created']

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
        ordering = ['-created']

    def __str__(self):
        return self.name
