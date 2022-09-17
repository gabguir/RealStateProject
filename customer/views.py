from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse

# Importación de models
from customer.models import Customer_Model

# Importación de forms
from customer.forms import Customer_Form


#=======================================================================================================================================
# Vistas para Clientes
#=======================================================================================================================================


def listar_clientes(request, *args, **kwargs):
    '''Lista clientes.'''
    
    object_list = Customer_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Clientes',
        'icon' : 'bx bxs-user-pin',
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
    
    itemObj = Customer_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de cliente',
        'icon' : 'bx bxs-user-pin',
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
        'icon' : 'bx bxs-user-pin',
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
    
    itemObj = Customer_Model.objects.get(id=id) 
    form = Customer_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Customer_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')

    context = {
        'page' : 'Editar cliente',
        'icon' : 'bx bxs-user-pin',
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
    
    itemObj = Customer_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_clientes')

    context = {
        'page' : 'Eliminar cliente',
        'icon' : 'bx bxs-user-pin',
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
    
