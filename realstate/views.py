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

# Importación de forms
from realstate.forms import Realstate_Form, Realstate_Type_Form


#=======================================================================================================================================
# Vistas para Inmuebles
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_inmuebles(request, *args, **kwargs):
    '''Lista inmuebles.'''
    
    object_list = Realstate_Model.objects.all() # Lista de objetos
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
        'page' : 'Inmuebles',
        'icon' : 'bx bxs-building-house',
        'info_agente': info_agente,
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)

@login_required(login_url='entrar')
def ver_inmueble(request, id, *args, **kwargs):
    '''Detalle de inmueble.'''
    
    itemObj = Realstate_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Detalle de inmueble',
        'icon' : 'bx bxs-building-house',
        'info_agente': info_agente,
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)

@login_required(login_url='entrar')
def crear_inmueble(request, *args, **kwargs):
    '''Crear inmueble.'''
    
    error_message = ''
    form = Realstate_Form()
    
    if request.method == 'POST':
        form = Realstate_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_inmuebles')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_inmuebles')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Crear inmueble',
        'icon' : 'bx bxs-building-house',
        'info_agente': info_agente,
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'error_message' : error_message,
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
@login_required(login_url='entrar')
def modificar_inmueble(request, id, *args, **kwargs):
    '''Editar inmueble.'''
    
    itemObj = Realstate_Model.objects.get(id=id) 
    form = Realstate_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Realstate_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_inmuebles')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_inmuebles')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Editar inmueble',
        'icon' : 'bx bxs-building-house',
        'info_agente': info_agente,
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)

@login_required(login_url='entrar')
def eliminar_inmueble(request, id, *args, **kwargs):
    '''Eliminar inmueble.'''
    
    itemObj = Realstate_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_inmuebles')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_inmuebles')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Eliminar inmueble',
        'icon' : 'bx bxs-building-house',
        'info_agente': info_agente,
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Categorías
#=======================================================================================================================================

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_tipo_inmuebles(request, *args, **kwargs):
    '''Lista inmuebles.'''
    
    object_list = Realstate_Type_Model.objects.all() # Lista de objetos
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
        'page' : 'Tipo de inmuebles',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'tipo de inmueble',
        'plural' : 'tipos de inmueble',
        'url_listar' : 'listar_tipo_inmuebles',
        'url_crear' : 'crear_tipo_inmueble',
        'url_ver' : 'ver_tipo_inmueble',
        'url_editar' : 'modificar_tipo_inmueble',
        'url_eliminar' : 'eliminar_tipo_inmueble',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def ver_tipo_inmueble(request, id, *args, **kwargs):
    '''Detalle de inmueble.'''
    
    itemObj = Realstate_Type_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Detalle de tipo de inmueble',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'tipo de inmueble',
        'plural' : 'tipos de inmueble',
        'url_listar' : 'listar_tipo_inmuebles',
        'url_crear' : 'crear_tipo_inmueble',
        'url_ver' : 'ver_tipo_inmueble',
        'url_editar' : 'modificar_tipo_inmueble',
        'url_eliminar' : 'eliminar_tipo_inmueble',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def crear_tipo_inmueble(request, *args, **kwargs):
    '''Crear inmueble.'''
    
    form = Realstate_Type_Form()
    
    if request.method == 'POST':
        form = Realstate_Type_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_tipo_inmuebles')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_tipo_inmuebles')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Crear tipo de inmueble',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'tipo de inmueble',
        'plural' : 'tipo de inmuebles',
        'url_listar' : 'listar_tipo_inmuebles',
        'url_crear' : 'crear_tipo_inmueble',
        'url_ver' : 'ver_tipo_inmueble',
        'url_editar' : 'modificar_tipo_inmueble',
        'url_eliminar' : 'eliminar_tipo_inmueble',
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)
    
@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def modificar_tipo_inmueble(request, id, *args, **kwargs):
    '''Editar inmueble.'''
    
    itemObj = Realstate_Type_Model.objects.get(id=id) 
    form = Realstate_Type_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Realstate_Type_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_tipo_inmuebles')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_tipo_inmuebles')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Editar tipo de inmueble',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'tipo de inmueble',
        'plural' : 'tipo de inmuebles',
        'url_listar' : 'listar_tipo_inmuebles',
        'url_crear' : 'crear_tipo_inmueble',
        'url_ver' : 'ver_tipo_inmueble',
        'url_editar' : 'modificar_tipo_inmueble',
        'url_eliminar' : 'eliminar_tipo_inmueble',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_form.html', context)

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def eliminar_tipo_inmueble(request, id, *args, **kwargs):
    '''Eliminar inmueble.'''
    
    itemObj = Realstate_Type_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_tipo_inmuebles')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_tipo_inmuebles')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Eliminar tipo de inmueble',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'tipo de inmueble',
        'plural' : 'tipos de inmueble',
        'url_listar' : 'listar_tipo_inmuebles',
        'url_crear' : 'crear_tipo_inmueble',
        'url_ver' : 'ver_tipo_inmueble',
        'url_editar' : 'modificar_tipo_inmueble',
        'url_eliminar' : 'eliminar_tipo_inmueble',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)

