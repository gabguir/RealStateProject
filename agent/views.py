from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse

# Importación de models
from agent.models import Agent_Model

# Importación de forms
from agent.forms import Agent_Form


#=======================================================================================================================================
# Vistas para Agentes
#=======================================================================================================================================


def listar_agentes(request, *args, **kwargs):
    '''Lista agentes.'''
    
    object_list = Agent_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Agentes',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_agente(request, id, *args, **kwargs):
    '''Detalle de agente.'''
    
    itemObj = Agent_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de agente',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_agente(request, *args, **kwargs):
    '''Crear agente.'''
    
    form = Agent_Form()
    
    if request.method == 'POST':
        form = Agent_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_agentes')

    context = {
        'page' : 'Crear agente',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_agente(request, id, *args, **kwargs):
    '''Editar agente.'''
    
    itemObj = Agent_Model.objects.get(id=id) 
    form = Agent_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Agent_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_agentes')

    context = {
        'page' : 'Editar agente',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_agente(request, id, *args, **kwargs):
    '''Eliminar agente.'''
    
    itemObj = Agent_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_agentes')

    context = {
        'page' : 'Eliminar agente',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)

