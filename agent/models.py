from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#=======================================================================================================================================
# Agent
#=======================================================================================================================================

class Agent_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre [*]')
    email = models.EmailField(max_length=254, verbose_name='Correo electrónico [*]')
    image_main = models.ImageField(upload_to='img_agent/', default='', verbose_name='Imagen [*]')
    description = RichTextField(null=True, blank=True, verbose_name='Descripción')
    
    url_twitter = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Twitter')
    url_facebook = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Facebook')
    url_linkedin = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Linkedin')
    url_instagram = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Instagram')
    # fk_user
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Usuario')
    draft = models.BooleanField(null=True, blank=True, default=True, verbose_name='Borrador')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos '''
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        ordering = ['-id']
    
    def __str__(self):
        # return str(self.user.username)
        return self.name
