#from ast import AsyncFunctionDef
from django.db.models import Q
from Models.models import Instalacion, Persona, Zona
#import calendar
from datetime import datetime, date, timedelta



def buscar_elementos(request, *args, **kwargs):

    buscar = ''
    if request.GET.get('buscar'):
        buscar = request.GET.get('buscar')

        fk_instalacion_guardia = Instalacion.objects.filter(name__icontains=buscar)

        queryset = Persona.objects.distinct().filter(
            Q(nombre_completo__icontains=buscar) |  
            Q(rut_dv_completo__icontains=buscar) |
            Q(fk_instalacion_guardia__in=fk_instalacion_guardia) 
            #& Q(fk_tipo_persona__in=fk_tipo_persona) 
            ).filter(activo=True).filter(fk_tipo_persona=6)
        #queryset = Persona.objects.filter(nombre_completo__icontains=buscar).filter(activo=True)

    else:
        #queryset = Persona.objects.all() # Lista de objetos
        queryset = Persona.objects.distinct().filter(activo=True) # Lista de objetos

    return queryset, buscar
    # MODO DE USO
    #queryset, buscar = buscar_personas(request, *args, **kwargs)
    pass



def buscar_personas(request, *args, **kwargs):

    buscar = ''
    if request.GET.get('buscar'):
        buscar = request.GET.get('buscar')
        #print(buscar)
        #queryset = Persona.objects.filter(activo=True)
        fk_instalacion_guardia = Instalacion.objects.filter(nombre__icontains=buscar)
        #fk_tipo_persona = Tipo_Persona.objects.filter(id__iexact=6)

        queryset = Persona.objects.distinct().filter(
            Q(nombre_completo__icontains=buscar) |  
            Q(rut_dv_completo__icontains=buscar) |
            Q(fk_instalacion_guardia__in=fk_instalacion_guardia) 
            #& Q(fk_tipo_persona__in=fk_tipo_persona) 
            ).filter(activo=True).filter(fk_tipo_persona=6)
        #queryset = Persona.objects.filter(nombre_completo__icontains=buscar).filter(activo=True)

    else:
        #queryset = Persona.objects.all() # Lista de objetos
        queryset = Persona.objects.distinct().filter(activo=True) # Lista de objetos

    return queryset, buscar
    # MODO DE USO
    #queryset, buscar = buscar_personas(request, *args, **kwargs)
    pass


def buscar_instalacion(request, *args, **kwargs):
    buscar = ''
    if request.GET.get('buscar'):
        buscar = request.GET.get('buscar')
        #print(buscar)

        #queryset = Instalacion.objects.filter(nombre__icontains=buscar).filter(activo=True)

        fk_zona = Zona.objects.filter(nombre__icontains=buscar)
        #fk_cliente = Cliente.objects.filter(nombre__icontains=buscar)

        queryset = Instalacion.objects.distinct().filter(
            Q(nombre__icontains=buscar) |  
            Q(codigo__icontains=buscar) |
            Q(fk_zona__in=fk_zona)
            ).filter(activo=True)

    else:
        #queryset = Persona.objects.all() # Lista de objetos
        queryset = Instalacion.objects.distinct().filter(activo=True) # Lista de objetos

    return queryset, buscar

    # MODO DE USO
    #queryset, buscar = buscar_instalacion(request, *args, **kwargs)
    pass
