from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse

# Importación de modelos
from Main.models import Property, Agent, Customer
from Main.models import Page, Article, Category, Image

# Importación de forms
from panel.forms import Property_Form, Agent_Form, Customer_Form
from panel.forms import Page_Form, Article_Form, Category_Form, Image_Form


#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

def app_panel_index(request, *args, **kwargs):
    '''Lista de elementos con las que se pueden realizar acciones.'''
    object_list = [
        {
            'object_title' : 'Inmuebles',
            'object_icon' : 'bx bxs-building-house',
            'object_description' : 'Agregar o modificar inmuebles',
            'object_url' : 'listar_inmuebles',
            # 'object_url' : '#',
        },
        {
            'object_title' : 'Agentes',
            'object_icon' : 'bx bxs-user-rectangle',
            'object_description' : 'Agregar o modificar agentes',
            'object_url' : 'listar_agentes',
            # 'object_url' : '#',
        },
        {
            'object_title' : 'Clientes',
            'object_icon' : 'bx bxs-user-pin',
            'object_description' : 'Agregar o modificar clientes',
            'object_url' : 'listar_clientes',
            # 'object_url' : '#',
        },
        {
            'object_title' : 'Páginas',
            'object_icon' : 'bx bxs-file',
            'object_description' : 'Agregar o modificar páginas',
            'object_url' : 'listar_paginas',
            # 'object_url' : '#',
        },
        {
            'object_title' : 'Artículos',
            'object_icon' : 'bx bx-file',
            'object_description' : 'Agregar o modificar articulos',
            'object_url' : 'listar_articulos',
        },
        {
            'object_title' : 'Categorías',
            'object_icon' : 'bx bxs-extension',
            'object_description' : 'Agregar o modificar categorías',
            'object_url' : 'listar_categorias',
            # 'object_url' : '',
        },
        {
            'object_title' : 'Imágenes',
            'object_icon' : 'bx bxs-image',
            'object_description' : 'Agregar o modificar imágenes',
            'object_url' : 'listar_imagenes',
            # 'object_url' : '#',
        },
    ]

    context = {
        'page' : 'Inicio',
        'icon' : '',
        'description' : 'Se pueden realizar acciones con los elementos listados a continuación.',
        'object_list' : object_list,
    }
    return render(request, 'panel/app_index.html', context)


#=======================================================================================================================================
# Vistas para Inmuebles
#=======================================================================================================================================

def listar_inmuebles(request, *args, **kwargs):
    '''Lista inmuebles.'''
    
    object_list = Property.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Inmuebles',
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_inmueble(request, id, *args, **kwargs):
    '''Detalle de inmueble.'''
    
    itemObj = Property.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de inmueble',
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


def crear_inmueble(request, *args, **kwargs):
    '''Crear inmueble.'''
    
    form = Property_Form()
    
    if request.method == 'POST':
        form = Property_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_inmuebles')

    context = {
        'page' : 'Crear inmueble',
        'singular' : 'inmueble',
        'plural' : 'inmuebles',
        'url_listar' : 'listar_inmuebles',
        'url_crear' : 'crear_inmueble',
        'url_ver' : 'ver_inmueble',
        'url_editar' : 'modificar_inmueble',
        'url_eliminar' : 'eliminar_inmueble',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_inmueble(request, id, *args, **kwargs):
    '''Editar inmueble.'''
    
    itemObj = Property.objects.get(id=id) 
    form = Property_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Property_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_inmuebles')

    context = {
        'page' : 'Editar inmueble',
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


def eliminar_inmueble(request, id, *args, **kwargs):
    '''Eliminar inmueble.'''
    
    itemObj = Property.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_inmuebles')

    context = {
        'page' : 'Eliminar inmueble',
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
# Vistas para Agentes
#=======================================================================================================================================

def listar_agentes(request, *args, **kwargs):
    '''Lista agentes.'''
    
    object_list = Agent.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Agentes',
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
    
    itemObj = Agent.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de agente',
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
    
    itemObj = Agent.objects.get(id=id) 
    form = Agent_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Agent_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_agentes')

    context = {
        'page' : 'Editar agente',
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
    
    itemObj = Agent.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_agentes')

    context = {
        'page' : 'Eliminar agente',
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

#=======================================================================================================================================
# Vistas para Clientes
#=======================================================================================================================================


def listar_clientes(request, *args, **kwargs):
    '''Lista clientes.'''
    
    object_list = Customer.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Clientes',
        'singular' : 'cliente',
        'plural' : 'clientes',
        'url_listar' : 'listar_clientes',
        'url_crear' : 'crear_cliente',
        'url_ver' : 'ver_cliente',
        'url_editar' : 'modificar_cliente',
        'url_eliminar' : 'eliminar_cliente',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_cliente(request, id, *args, **kwargs):
    '''Detalle de cliente.'''
    
    itemObj = Customer.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de cliente',
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


def crear_cliente(request, *args, **kwargs):
    '''Crear cliente.'''
    
    form = Customer_Form()
    
    if request.method == 'POST':
        form = Customer_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    context = {
        'page' : 'Crear cliente',
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
    
    
def modificar_cliente(request, id, *args, **kwargs):
    '''Editar cliente.'''
    
    itemObj = Customer.objects.get(id=id) 
    form = Customer_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Customer_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    context = {
        'page' : 'Editar cliente',
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


def eliminar_cliente(request, id, *args, **kwargs):
    '''Eliminar cliente.'''
    
    itemObj = Customer.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_clientes')

    context = {
        'page' : 'Eliminar cliente',
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
    


#=======================================================================================================================================
# Vistas para Páginas
#=======================================================================================================================================

def listar_paginas(request, *args, **kwargs):
    '''Lista páginas.'''
    
    # object_list = Page.objects.filter(draft=False) # Lista de objetos
    object_list = Page.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Páginas',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'listar_paginas',
        'url_crear' : 'crear_pagina',
        'url_ver' : 'ver_pagina',
        'url_editar' : 'modificar_pagina',
        'url_eliminar' : 'eliminar_pagina',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_pagina(request, id, *args, **kwargs):
    '''Detalle de página.'''
    
    itemObj = Page.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de página',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'listar_paginas',
        'url_crear' : 'crear_pagina',
        'url_ver' : 'ver_pagina',
        'url_editar' : 'modificar_pagina',
        'url_eliminar' : 'eliminar_pagina',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_pagina(request, *args, **kwargs):
    '''Crear página.'''
    
    form = Page_Form()
    
    if request.method == 'POST':
        form = Page_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_paginas')

    context = {
        'page' : 'Crear página',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'listar_paginas',
        'url_crear' : 'crear_pagina',
        'url_ver' : 'ver_pagina',
        'url_editar' : 'modificar_pagina',
        'url_eliminar' : 'eliminar_pagina',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_pagina(request, id, *args, **kwargs):
    '''Editar página.'''
    
    itemObj = Page.objects.get(id=id) 
    form = Article_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Page_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_paginas')

    context = {
        'page' : 'Editar página',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'listar_paginas',
        'url_crear' : 'crear_pagina',
        'url_ver' : 'ver_pagina',
        'url_editar' : 'modificar_pagina',
        'url_eliminar' : 'eliminar_pagina',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_pagina(request, id, *args, **kwargs):
    '''Eliminar página.'''
    
    itemObj = Page.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_paginas')

    context = {
        'page' : 'Eliminar página',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'listar_paginas',
        'url_crear' : 'crear_pagina',
        'url_ver' : 'ver_pagina',
        'url_editar' : 'modificar_pagina',
        'url_eliminar' : 'eliminar_pagina',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)

#=======================================================================================================================================
# Vistas para Artículos
#=======================================================================================================================================

def listar_articulos(request, *args, **kwargs):
    '''Lista artículos.'''
    
    object_list = Article.objects.filter(draft=False) # Lista de objetos
    
    context = {
        'page' : 'Artículos',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_articulo(request, id, *args, **kwargs):
    '''Detalle de artículo.'''
    
    itemObj = Article.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Artículo',
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


def crear_articulo(request, *args, **kwargs):
    '''Crear artículo.'''
    
    form = Article_Form()
    
    if request.method == 'POST':
        form = Article_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')

    context = {
        'page' : 'Crear Artículo',
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
    
    
def modificar_articulo(request, id, *args, **kwargs):
    '''Editar artículo.'''
    
    itemObj = Article.objects.get(id=id) 
    form = Article_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Article_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')

    context = {
        'page' : 'Editar Artículo',
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


def activar_articulo(request, id, *args, **kwargs):
    '''Activar artículo.'''
    
    itemObj = Article.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.draft = '1'
        itemObj.save()
        return redirect('listar_articulos')

    context = {
        'page' : 'Activar Artículo',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'item': itemObj,
    }
    return render(request, 'panel/generic_activate_object.html', context)


def desactivar_articulo(request, id, *args, **kwargs):
    '''Desactivar artículo.'''
    
    itemObj = Article.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.draft = '0'
        itemObj.save()
        return redirect('listar_articulos')

    context = {
        'page' : 'Activar Artículo',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'url_crear' : 'crear_articulo',
        'url_ver' : 'ver_articulo',
        'url_editar' : 'modificar_articulo',
        'url_eliminar' : 'eliminar_articulo',
        'item': itemObj,
    }
    return render(request, 'panel/generic_deactivate_object.html', context)
    
    
def eliminar_articulo(request, id, *args, **kwargs):
    '''Eliminar artículo.'''
    
    itemObj = Article.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_articulos')

    context = {
        'page' : 'Eliminar Artículo',
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

def listar_categorias(request, *args, **kwargs):
    '''Lista categorías.'''
    
    object_list = Category.objects.all() # Lista de objetos
    
    context = {
        'page' : 'categorías',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_categoria(request, id, *args, **kwargs):
    '''Detalle de categoría.'''
    
    itemObj = Category.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de categoría',
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


def crear_categoria(request, *args, **kwargs):
    '''Crear categoría.'''
    
    form = Category_Form()
    
    if request.method == 'POST':
        form = Category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')

    context = {
        'page' : 'Crear categoría',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'listar_categorias',
        'url_crear' : 'crear_categoria',
        'url_ver' : 'ver_categoria',
        'url_editar' : 'modificar_categoria',
        'url_eliminar' : 'eliminar_categoria',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_categoria(request, id, *args, **kwargs):
    '''Editar categoría.'''
    
    itemObj = Category.objects.get(id=id) 
    form = Category_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Category_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')

    context = {
        'page' : 'Editar categoría',
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
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_categoria(request, id, *args, **kwargs):
    '''Eliminar categoría.'''
    
    itemObj = Category.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_categorias')

    context = {
        'page' : 'Eliminar categoría',
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

#=======================================================================================================================================
# Vistas para Imágenes
#=======================================================================================================================================

def listar_imagenes(request, *args, **kwargs):
    '''Lista imágenes.'''
    
    object_list = Image.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Imágenes',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_activo_index' : 'listar_imagenes',
        'url_crear' : 'crear_imagen',
        'url_ver' : 'ver_imagen',
        'url_editar' : 'modificar_imagen',
        'url_eliminar' : 'eliminar_imagen',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_imagen(request, id, *args, **kwargs):
    '''Detalle de imagen.'''
    
    itemObj = Image.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'listar_imagenes',
        'url_crear' : 'crear_imagen',
        'url_ver' : 'ver_imagen',
        'url_editar' : 'modificar_imagen',
        'url_eliminar' : 'eliminar_imagen',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_imagen(request, *args, **kwargs):
    '''Crear imagen.'''
    
    form = Image_Form()
    
    if request.method == 'POST':
        form = Image_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_imagenes')

    context = {
        'page' : 'Crear imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'listar_imagenes',
        'url_crear' : 'crear_imagen',
        'url_ver' : 'ver_imagen',
        'url_editar' : 'modificar_imagen',
        'url_eliminar' : 'eliminar_imagen',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_imagen(request, id, *args, **kwargs):
    '''Editar imagen.'''
    
    itemObj = Image.objects.get(id=id) 
    form = Image_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Image_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_imagenes')

    context = {
        'page' : 'Editar imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'listar_imagenes',
        'url_crear' : 'crear_imagen',
        'url_ver' : 'ver_imagen',
        'url_editar' : 'modificar_imagen',
        'url_eliminar' : 'eliminar_imagen',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_imagen(request, id, *args, **kwargs):
    '''Eliminar imagen.'''
    
    itemObj = Image.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_imagenes')

    context = {
        'page' : 'Eliminar imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'listar_imagenes',
        'url_crear' : 'crear_imagen',
        'url_ver' : 'ver_imagen',
        'url_editar' : 'modificar_imagen',
        'url_eliminar' : 'eliminar_imagen',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)