from django.db import models

#=======================================================================================================================================
# Customer
#=======================================================================================================================================

class Customer_Model(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre [*]')
    email = models.EmailField(max_length=254, verbose_name='Correo electrónico [*]')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos '''
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.name
