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
from customer.models import Customer_Model
from agent.models import Agent_Model

# Importación de forms
from customer.forms import Customer_Form


#=======================================================================================================================================
# Vistas para Clientes
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_clientes(request, *args, **kwargs):
    '''Lista clientes.'''
    
    object_list = Customer_Model.objects.all() # Lista de objetos
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
        'page' : 'Clientes',
        'icon' : 'bx bxs-user-pin',
        'info_agente': info_agente,
        'singular' : 'cliente',
        'plural' : 'clientes',
        'url_listar' : 'listar_clientes',
        'url_crear' : 'crear_cliente',
        'url_ver' : 'ver_cliente',
        'url_editar' : 'modificar_cliente',
        'url_eliminar' : 'eliminar_cliente',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)

@login_required(login_url='entrar')
def ver_cliente(request, id, *args, **kwargs):
    '''Detalle de cliente.'''
    
    itemObj = Customer_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Detalle de cliente',
        'icon' : 'bx bxs-user-pin',
        'info_agente': info_agente,
        'singular' : 'cliente',
        'plural' : 'clientes',
        'url_listar' : 'listar_clientes',
        'url_crear' : 'crear_cliente',
        'url_ver' : 'ver_cliente',
        'url_editar' : 'modificar_cliente',
        'url_eliminar' : 'eliminar_cliente',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)

@login_required(login_url='entrar')
def crear_cliente(request, *args, **kwargs):
    '''Crear cliente.'''
    
    form = Customer_Form()
    
    if request.method == 'POST':
        form = Customer_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_clientes')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_clientes')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Crear cliente',
        'icon' : 'bx bxs-user-pin',
        'info_agente': info_agente,
        'singular' : 'cliente',
        'plural' : 'clientes',
        'url_listar' : 'listar_clientes',
        'url_crear' : 'crear_cliente',
        'url_ver' : 'ver_cliente',
        'url_editar' : 'modificar_cliente',
        'url_eliminar' : 'eliminar_cliente',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
@login_required(login_url='entrar')
def modificar_cliente(request, id, *args, **kwargs):
    '''Editar cliente.'''
    
    itemObj = Customer_Model.objects.get(id=id) 
    form = Customer_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Customer_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_clientes')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_clientes')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Editar cliente',
        'icon' : 'bx bxs-user-pin',
        'info_agente': info_agente,
        'singular' : 'cliente',
        'plural' : 'clientes',
        'url_listar' : 'listar_clientes',
        'url_crear' : 'crear_cliente',
        'url_ver' : 'ver_cliente',
        'url_editar' : 'modificar_cliente',
        'url_eliminar' : 'eliminar_cliente',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)

@login_required(login_url='entrar')
def eliminar_cliente(request, id, *args, **kwargs):
    '''Eliminar cliente.'''
    
    itemObj = Customer_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_clientes')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_clientes')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Eliminar cliente',
        'icon' : 'bx bxs-user-pin',
        'info_agente': info_agente,
        'singular' : 'cliente',
        'plural' : 'clientes',
        'url_listar' : 'listar_clientes',
        'url_crear' : 'crear_cliente',
        'url_ver' : 'ver_cliente',
        'url_editar' : 'modificar_cliente',
        'url_eliminar' : 'eliminar_cliente',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
    
