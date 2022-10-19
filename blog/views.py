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
from blog.models import Article_Model, Category_Model

# Importación de forms
from blog.forms import Article_Form, Category_Form


#=======================================================================================================================================
# Vistas para Artículos
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_articulos(request, *args, **kwargs):
    '''Lista artículos.'''
    
    object_list = Article_Model.objects.all() # Lista de objetos
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
        'page' : 'Artículos',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)

@login_required(login_url='entrar')
def ver_articulo(request, id, *args, **kwargs):
    '''Detalle de artículo.'''
    
    itemObj = Article_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Detalle de Artículo',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)

@login_required(login_url='entrar')
def crear_articulo(request, *args, **kwargs):
    '''Crear artículo.'''
    
    form = Article_Form()
    
    if request.method == 'POST':
        form = Article_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_articulos')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            #return redirect('listar_articulos')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Crear Artículo',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)

@login_required(login_url='entrar')
def modificar_articulo(request, id, *args, **kwargs):
    '''Editar artículo.'''
    
    itemObj = Article_Model.objects.get(id=id) 
    print(f'itemObj: {itemObj}')
    form = Article_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Article_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_articulos')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_articulos')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Editar Artículo',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)

@login_required(login_url='entrar')
def eliminar_articulo(request, id, *args, **kwargs):
    '''Eliminar artículo.'''
    
    itemObj = Article_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_articulos')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_articulos')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Eliminar Artículo',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
    



#=======================================================================================================================================
# Vistas para Categorías
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_categorias(request, *args, **kwargs):
    '''Lista categorías.'''
    
    object_list = Category_Model.objects.all() # Lista de objetos
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
        'page' : 'Categorías',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)

@login_required(login_url='entrar')
def ver_categoria(request, id, *args, **kwargs):
    '''Detalle de categoría.'''
    
    itemObj = Category_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Detalle de categoría',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)

@login_required(login_url='entrar')
def crear_categoria(request, *args, **kwargs):
    '''Crear categoría.'''
    
    form = Category_Form()
    
    if request.method == 'POST':
        form = Category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_categorias')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_categorias')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Crear categoría',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)
    
@login_required(login_url='entrar')
def modificar_categoria(request, id, *args, **kwargs):
    '''Editar categoría.'''
    
    itemObj = Category_Model.objects.get(id=id) 
    form = Category_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Category_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_categorias')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            # return redirect('listar_categorias')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Editar categoría',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_form.html', context)

@login_required(login_url='entrar')
def eliminar_categoria(request, id, *args, **kwargs):
    '''Eliminar categoría.'''
    
    itemObj = Category_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_categorias')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_categorias')

    info_agente = info_header_agente(request)

    context = {
        'page' : 'Eliminar categoría',
        'icon' : 'bx bxs-extension',
        'info_agente': info_agente,
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)


