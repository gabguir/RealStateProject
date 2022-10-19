from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from urllib.parse import urlencode

# importación de funcionalidad para login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
# importar custom decorators
from panel.decorators import authenticated_user, allowed_users


from panel.utils import info_header_agente

# Importación de models
from agent.models import Agent_Model
from realstate.models import Realstate_Model, Realstate_Type_Model
from blog.models import Article_Model

# Importación de forms
from agent.forms import Agent_Form


#=======================================================================================================================================
# Vistas para Agentes
#=======================================================================================================================================

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_agentes(request, *args, **kwargs):
    '''Lista agentes.'''
    
    object_list = Agent_Model.objects.all() # Lista de objetos
    # Mensajes para el usuario
    success_create = ''
    success_edit = ''
    success_delete = ''
    if request.method == 'GET':
        success_create_get = request.GET.get('success_create')
        print(f'success_create_get: {success_create_get}')
        if success_create_get == 'OK':
            success_create = 'OK'
        success_edit_get = request.GET.get('success_edit')
        print(f'success_edit_get: {success_edit_get}')
        if success_edit_get == 'OK':
            success_edit = 'OK'
        success_delete_get = request.GET.get('success_delete')
        print(f'success_delete_get: {success_delete_get}')
        if success_delete_get == 'OK':
            success_delete = 'OK'
            
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Agentes',
        'icon' : 'bx bxs-user-rectangle',
        'info_agente': info_agente,
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def ver_agente(request, id, *args, **kwargs):
    '''Detalle de agente.'''
    
    itemObj = Agent_Model.objects.get(id=id) 
    agente_inmuebles = Realstate_Model.objects.filter(fk_agent=id).order_by('-date')
    agente_articulos = Article_Model.objects.filter(fk_agent=id).order_by('-date')
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Detalle de agente',
        'icon' : 'bx bxs-user-rectangle',
        'info_agente': info_agente,
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_listar' : 'listar_agentes',
        'url_crear' : 'crear_agente',
        'url_ver' : 'ver_agente',
        'url_editar' : 'modificar_agente',
        'url_eliminar' : 'eliminar_agente',
        'agente_inmuebles': agente_inmuebles,
        'agente_articulos': agente_articulos,
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def crear_agente(request, *args, **kwargs):
    '''Crear agente.'''
    
    form = Agent_Form()
    
    if request.method == 'POST':
        form = Agent_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_agentes')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_agentes')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Crear agente',
        'icon' : 'bx bxs-user-rectangle',
        'info_agente': info_agente,
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


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def modificar_agente(request, id, *args, **kwargs):
    '''Editar agente.'''
    
    itemObj = Agent_Model.objects.get(id=id) 
    form = Agent_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Agent_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_agentes')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_agentes')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Editar agente',
        'icon' : 'bx bxs-user-rectangle',
        'info_agente': info_agente,
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


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def eliminar_agente(request, id, *args, **kwargs):
    '''Eliminar agente.'''
    
    itemObj = Agent_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_agentes')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_agentes')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Eliminar agente',
        'icon' : 'bx bxs-user-rectangle',
        'info_agente': info_agente,
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

