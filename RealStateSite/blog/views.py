from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse

# Importación de models
from blog.models import Article_Model, Category_Model
from agent.models import Agent_Model

# Importación de forms
from blog.forms import Article_Form, Category_Form


#=======================================================================================================================================
# Vistas para Artículos
#=======================================================================================================================================


def listar_articulos(request, *args, **kwargs):
    '''Lista artículos.'''
    
    object_list = Article_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Artículos',
        'icon' : 'bx bx-file',
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
    
    itemObj = Article_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Artículo',
        'icon' : 'bx bx-file',
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
        'icon' : 'bx bx-file',
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
    
    itemObj = Article_Model.objects.get(id=id) 
    print(f'itemObj: {itemObj}')
    form = Article_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Article_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')

    context = {
        'page' : 'Editar Artículo',
        'icon' : 'bx bx-file',
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


# def activar_articulo(request, id, *args, **kwargs):
#     '''Activar artículo.'''
    
#     itemObj = Article_Model.objects.get(id=id) 
    
#     if request.method == 'POST':
#         itemObj.draft = '1'
#         itemObj.save()
#         return redirect('listar_articulos')

#     context = {
#         'page' : 'Activar Artículo',
#         'icon' : 'bx bx-file',
#         'singular' : 'artículo',
#         'plural' : 'artículos',
#         'url_listar' : 'listar_articulos',
#         'url_crear' : 'crear_articulo',
#         'url_ver' : 'ver_articulo',
#         'url_editar' : 'modificar_articulo',
#         'url_eliminar' : 'eliminar_articulo',
#         'item': itemObj,
#     }
#     return render(request, 'panel/generic_activate_object.html', context)


# def desactivar_articulo(request, id, *args, **kwargs):
#     '''Desactivar artículo.'''
    
#     itemObj = Article_Model.objects.get(id=id) 
    
#     if request.method == 'POST':
#         itemObj.draft = '0'
#         itemObj.save()
#         return redirect('listar_articulos')

#     context = {
#         'page' : 'Activar Artículo',
#         'icon' : 'bx bx-file',
#         'singular' : 'artículo',
#         'plural' : 'artículos',
#         'url_listar' : 'listar_articulos',
#         'url_crear' : 'crear_articulo',
#         'url_ver' : 'ver_articulo',
#         'url_editar' : 'modificar_articulo',
#         'url_eliminar' : 'eliminar_articulo',
#         'item': itemObj,
#     }
#     return render(request, 'panel/generic_deactivate_object.html', context)
    
    
def eliminar_articulo(request, id, *args, **kwargs):
    '''Eliminar artículo.'''
    
    itemObj = Article_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_articulos')

    context = {
        'page' : 'Eliminar Artículo',
        'icon' : 'bx bx-file',
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
    
    object_list = Category_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Categorías',
        'icon' : 'bx bxs-extension',
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
    
    itemObj = Category_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de categoría',
        'icon' : 'bx bxs-extension',
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
        'icon' : 'bx bxs-extension',
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
    
    
def modificar_categoria(request, id, *args, **kwargs):
    '''Editar categoría.'''
    
    itemObj = Category_Model.objects.get(id=id) 
    form = Category_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Category_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')

    context = {
        'page' : 'Editar categoría',
        'icon' : 'bx bxs-extension',
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


def eliminar_categoria(request, id, *args, **kwargs):
    '''Eliminar categoría.'''
    
    itemObj = Category_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_categorias')

    context = {
        'page' : 'Eliminar categoría',
        'icon' : 'bx bxs-extension',
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

# def listar_imagenes(request, *args, **kwargs):
#     '''Lista imágenes.'''
    
#     object_list = Image_Article_Model.objects.all() # Lista de objetos
    
#     context = {
#         'page' : 'Imágenes',
#         'singular' : 'imagen',
#         'plural' : 'imágenes',
#         'url_activo_index' : 'listar_imagenes',
#         'url_crear' : 'crear_imagen',
#         'url_ver' : 'ver_imagen',
#         'url_editar' : 'modificar_imagen',
#         'url_eliminar' : 'eliminar_imagen',
#         'object_list': object_list
#     }
#     return render(request, 'panel/generic_list.html', context)


# def ver_imagen(request, id, *args, **kwargs):
#     '''Detalle de imagen.'''
    
#     itemObj = Image_Article_Model.objects.filter(id=id) 
    
#     context = {
#         'page' : 'Detalle de imagen',
#         'singular' : 'imagen',
#         'plural' : 'imágenes',
#         'url_listar' : 'listar_imagenes',
#         'url_crear' : 'crear_imagen',
#         'url_ver' : 'ver_imagen',
#         'url_editar' : 'modificar_imagen',
#         'url_eliminar' : 'eliminar_imagen',
#         'item': itemObj
#     }
#     return render(request, 'panel/generic_detail.html', context)


# def crear_imagen(request, *args, **kwargs):
#     '''Crear imagen.'''
    
#     form = Image_Article_Form()
    
#     if request.method == 'POST':
#         form = Image_Article_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_imagenes')

#     context = {
#         'page' : 'Crear imagen',
#         'singular' : 'imagen',
#         'plural' : 'imágenes',
#         'url_listar' : 'listar_imagenes',
#         'url_crear' : 'crear_imagen',
#         'url_ver' : 'ver_imagen',
#         'url_editar' : 'modificar_imagen',
#         'url_eliminar' : 'eliminar_imagen',
#         'form': form
#     }
#     return render(request, 'panel/generic_file_form.html', context)
    
    
# def modificar_imagen(request, id, *args, **kwargs):
#     '''Editar imagen.'''
    
#     itemObj = Image_Article_Model.objects.get(id=id) 
#     form = Image_Article_Form(instance=itemObj)
    
#     if request.method == 'POST':
#         form = Image_Article_Form(request.POST, request.FILES, instance=itemObj)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_imagenes')

#     context = {
#         'page' : 'Editar imagen',
#         'singular' : 'imagen',
#         'plural' : 'imágenes',
#         'url_listar' : 'listar_imagenes',
#         'url_crear' : 'crear_imagen',
#         'url_ver' : 'ver_imagen',
#         'url_editar' : 'modificar_imagen',
#         'url_eliminar' : 'eliminar_imagen',
#         'item': itemObj,
#         'form': form,
#     }
#     return render(request, 'panel/generic_file_form.html', context)


# def eliminar_imagen(request, id, *args, **kwargs):
#     '''Eliminar imagen.'''
    
#     itemObj = Image_Article_Model.objects.get(id=id) 
    
#     if request.method == 'POST':
#         itemObj.delete()
#         return redirect('listar_imagenes')

#     context = {
#         'page' : 'Eliminar imagen',
#         'singular' : 'imagen',
#         'plural' : 'imágenes',
#         'url_listar' : 'listar_imagenes',
#         'url_crear' : 'crear_imagen',
#         'url_ver' : 'ver_imagen',
#         'url_editar' : 'modificar_imagen',
#         'url_eliminar' : 'eliminar_imagen',
#         'item': itemObj,
#     }
#     return render(request, 'panel/generic_delete_object.html', context)

