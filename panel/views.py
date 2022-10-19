from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q

# importación de funcionalidad para creación de usuarios
from django.contrib.auth.forms import UserCreationForm

# importación de funcionalidad para login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

# importar custom decorators
from panel.decorators import authenticated_user, allowed_users

# Importar modelos desde apps de backend
from agent.models import Agent_Model
from blog.models import Article_Model, Category_Model
from customer.models import Customer_Model
from realstate.models import Realstate_Model, Realstate_Type_Model, Message_Realstate_Model
from panel.models import Page_Model, Backend_Search_Model, Frontend_Search_Model, Message_Contact_Model, Message_Agent_Model

# Importación de forms
from agent.forms import Agent_Form
from blog.forms import Article_Form, Category_Form
from customer.forms import Customer_Form
from realstate.forms import Realstate_Form, Realstate_Type_Form, Message_Realstate_Form
from panel.forms import Page_Form, Backend_Search_Form, Frontend_Search_Form, Message_Contact_Form, CustomUserCreationForm, Message_Agent_Form

from panel.utils import info_header_agente

#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

@login_required(login_url='entrar')
def app_panel_index(request, *args, **kwargs):
    '''Lista de elementos con las que se pueden realizar acciones.'''
    elementos = [
        {
            'object_title' : 'Inmuebles',
            'icon' : 'bi bi-house-heart',
            'object_description' : 'Agregar, modificar o eliminar inmuebles.',
            'url_listar' : 'listar_inmuebles',
            'url_crear' : 'crear_inmueble',
        },
        {
            'object_title' : 'Tipo de inmueble',
            'icon' : 'bi bi-building',
            'object_description' : 'Agregar, modificar o eliminar tipos de inmueble.',
            'url_listar' : 'listar_tipo_inmuebles',
            'url_crear' : 'crear_tipo_inmueble',
        },
        {
            'object_title' : 'Agentes',
            'icon' : 'bi bi-person',
            'object_description' : 'Agregar, modificar o eliminar agentes.',
            'url_listar' : 'listar_agentes',
            'url_crear' : 'crear_agente',
        },
        {
            'object_title' : 'Clientes',
            'icon' : 'bi bi-people',
            'object_description' : 'Agregar, modificar o eliminar clientes.',
            'url_listar' : 'listar_clientes',
            'url_crear' : 'crear_cliente',
        },
        {
            'object_title' : 'Páginas',
            'icon' : 'bx bxs-file',
            'object_description' : 'Agregar, modificar o eliminar páginas.',
            'url_listar' : 'listar_paginas',
            'url_crear' : 'crear_pagina',
        },
        {
            'object_title' : 'Artículos',
            'icon' : 'bi bi-file-richtext',
            'object_description' : 'Agregar, modificar o eliminar articulos.',
            'url_listar' : 'listar_articulos',
            'url_crear' : 'crear_articulo',
        },
        {
            'object_title' : 'Categorías',
            'icon' : 'bi bi-tags',
            'object_description' : 'Agregar, modificar o eliminar categorías.',
            'url_listar' : 'listar_categorias',
            'url_crear' : 'crear_categoria',
        },
    ]
    funcionalidades = [
        {
            'object_title' : 'Mensajes de agentes',
            'icon' : 'bi bi-envelope-paper-heart',
            'object_description' : 'Revisar o eliminar mensajes de agentes.',
            'url_listar' : 'listar_mensajes_agente',
        },
        {
            'object_title' : 'Mensajes de propiedades',
            'icon' : 'bi bi-envelope-paper-heart',
            'object_description' : 'Revisar o eliminar mensajes de propiedades.',
            'url_listar' : 'listar_mensajes_inmueble',
        },
        {
            'object_title' : 'Mensajes de contacto',
            'icon' : 'bi bi-envelope-paper-heart',
            'object_description' : 'Revisar o eliminar mensajesde contacto.',
            'url_listar' : 'listar_mensajes_contacto',
        },
        {
            'object_title' : 'Búsqueda de sitio web',
            'icon' : 'bi bi-search',
            'object_description' : 'Revisar o eliminar búsquedas realizadas en el sitio web.',
            'url_listar' : 'listar_busquedas_frontend',
        },
        {
            'object_title' : 'Búsqueda de panel admin',
            'icon' : 'bi bi-search',
            'object_description' : 'Revisar o eliminar búsquedas realizadas en el panel de administración.',
            'url_listar' : 'listar_busquedas_backend',
        },
    ]

    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    count_inmuebles = Realstate_Model.objects.all().count()
    count_inmuebles_activos = Realstate_Model.objects.filter(draft=False).count()
    count_inmuebles_inactivos = Realstate_Model.objects.filter(draft=True).count()
    count_clientes = Customer_Model.objects.all().count()
    count_agentes = Agent_Model.objects.all().count()
    count_articulos = Article_Model.objects.all().count()
    count_articulos_activos = Article_Model.objects.filter(draft=False).count()
    count_articulos_inactivos = Article_Model.objects.filter(draft=True).count()
    count_paginas = Page_Model.objects.all().count()
    count_categorias = Category_Model.objects.all().count()

    inmuebles_activos = Realstate_Model.objects.filter(draft=False).order_by('-date')[:3]
    articulos_activos = Article_Model.objects.filter(draft=False).order_by('-date')[:3]
    agentes_activos = Agent_Model.objects.filter(draft=False)
    
    user_actual = request.user.id
    print(f'user_actual: {request.user}')
    
    mensajes_contacto = Message_Contact_Model.objects.all().order_by('-created')[:3]
    count_mensajes_contacto = mensajes_contacto.count()
    
    info_agente = info_header_agente(request)
    #print(f'info_agente: {info_agente}')
    
    # inmuebles de este agente
    inmuebles_agente = Realstate_Model.objects.filter(fk_agent=info_agente).order_by('-date')
    mensajes_inmueble = Message_Realstate_Model.objects.filter(id__in=inmuebles_agente).order_by('-created')
    count_mensajes_inmueble = mensajes_inmueble.count()
    print(f'inmuebles_agente:{inmuebles_agente}')
    print(f'mensajes_inmueble:{mensajes_inmueble}')
        
    # mensajes hacia este agente
    mensajes_agente = Message_Agent_Model.objects.filter(agent_receiver=info_agente).order_by('-created')[:3]
    count_mensajes_agente = mensajes_agente.count()
    print(f'mensajes_agente:{mensajes_agente}')
    
    
    context = {
        'page' : 'Inicio',
        'icon' : 'bi bi-grid',
        'info_agente': info_agente,
        'count_inmuebles': count_inmuebles,
        'count_inmuebles_activos': count_inmuebles_activos,
        'count_inmuebles_inactivos': count_inmuebles_inactivos,
        'count_clientes': count_clientes,
        'count_agentes': count_agentes,
        'count_articulos': count_articulos,
        'count_articulos_activos': count_articulos_activos,
        'count_articulos_inactivos': count_articulos_inactivos,
        'count_paginas': count_paginas,
        'count_categorias': count_categorias,
        'inmuebles': inmuebles_activos,
        'articulos': articulos_activos,
        'agentes_activos': agentes_activos,
        'mensajes_contacto': mensajes_contacto,
        'count_mensajes_contacto': count_mensajes_contacto,
        'mensajes_inmueble': mensajes_inmueble,
        'count_mensajes_inmueble': count_mensajes_inmueble,
        'mensajes_agente': mensajes_agente,
        'count_mensajes_agente': count_mensajes_agente,
        'elementos' : elementos,
        'funcionalidades' : funcionalidades,
    }
    if group == 'admin':
        return render(request, 'panel/app_index.html', context)
    elif group == 'agent':
        return render(request, 'panel/dashboard_agent.html', context)

@login_required(login_url='entrar')
def resultados_busqueda(request, *args, **kwargs):
    '''Muestra resultados de búsqueda.'''
    form = Backend_Search_Form()
    vacio = True
    termino_busqueda = ''
    result_inmueble = ''
    result_agente = ''
    result_cliente = ''
    result_pagina = ''
    result_articulo = ''
    result_categoria = ''
    result_imagen = ''
    
    if request.method == 'POST':
        form = Backend_Search_Form(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['name']
            print(termino_busqueda)
            form.save()

        if termino_busqueda == '':
            vacio = True
        else:
            vacio = False
            result_inmueble = Realstate_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(address__icontains=termino_busqueda) |
                Q(price__icontains=termino_busqueda) |
                Q(location__icontains=termino_busqueda) 
                )
            result_agente = Agent_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(email__icontains=termino_busqueda) |
                Q(description__icontains=termino_busqueda) 
                )
            result_cliente = Customer_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(email__icontains=termino_busqueda) 
                )
            result_pagina = Page_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(title__icontains=termino_busqueda) |
                Q(subtitle__icontains=termino_busqueda) |
                Q(abstract__icontains=termino_busqueda) |
                Q(content__icontains=termino_busqueda)
                )
            result_articulo = Article_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(title__icontains=termino_busqueda) |
                Q(subtitle__icontains=termino_busqueda) |
                Q(abstract__icontains=termino_busqueda) |
                Q(content__icontains=termino_busqueda)
                )
            result_categoria = Category_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(description__icontains=termino_busqueda) 
                )


            # print('termino_busqueda: ', termino_busqueda)
            # print('result_inmueble: ', result_inmueble)
            # print('result_agente: ', result_agente)
            # print('result_cliente: ', result_cliente)
            # print('result_pagina: ', result_pagina)
            # print('result_articulo: ', result_articulo)
            # print('result_categoria: ', result_categoria)
            # print('result_imagen: ', result_imagen)
    info_agente = info_header_agente(request)
    
    context = {
        'page': 'Resultados de búsqueda',
        'icon': 'bi bi-grid',
        'info_agente': info_agente,
        'termino_busqueda': termino_busqueda,
        'vacio': vacio,
        'result_inmueble': result_inmueble,
        'result_agente': result_agente,
        'result_cliente': result_cliente,
        'result_pagina': result_pagina,
        'result_articulo': result_articulo,
        'result_categoria': result_categoria,
    }
    return render(request, 'panel/search_result.html', context)


@login_required(login_url='entrar')
def ayuda(request, *args, **kwargs):
    '''Ayuda'''
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Ayuda',
        #'object_list': object_list,
        'info_agente': info_agente,
    }
    return render(request, 'panel/ayuda.html', context)
    


#=======================================================================================================================================
# Login
#=======================================================================================================================================

@login_required(login_url='entrar')
def test(request, *args, **kwargs):
    '''Test'''
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Login',
        #'object_list': object_list,
        'info_agente': info_agente,
    }
    #return render(request, 'panel/error_404.html', context)
    return render(request, 'login/register_user.html', context)


@authenticated_user
def entrar(request, *args, **kwargs):
    '''Página de Login de la plataforma. '''
    # Sacar al usuario que ingresa a esta vista
    #logout(request)
    
    # Mensajes para el usuario
    status = ''
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # loguear al usuario con el usuario recién creado
                login(request, user)
                return redirect('app_panel_index')
            else:
                base_url = reverse('entrar')  
                query_string =  urlencode({'status': 'ERROR'})  
                url = '{}?{}'.format(base_url, query_string)  
                return redirect(url) 
                #return redirect('entrar')
        else:
            base_url = reverse('entrar')  
            query_string =  urlencode({'status': 'ERROR'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            #return redirect('entrar')

    if request.method == 'GET':
        status_get = request.GET.get('status')
        print(f'status_get: {status_get}')
        if status_get == 'ERROR':
            status = 'ERROR'
            
        status_get = request.GET.get('status')
        print(f'status_get: {status_get}')
        if status_get == 'SALIR':
            status = 'SALIR'
        
    form = AuthenticationForm()

    
    context = {
        'page': 'Acceso / Login',
        'status': status,
        'form': form,
    }
    

    return render(request, 'login/login.html', context)


def salir(request, *args, **kwargs):
    logout(request)
    return redirect('entrar')



#=======================================================================================================================================
# Vistas para Perfil
#=======================================================================================================================================

@login_required(login_url='entrar')
def ver_perfil(request, *args, **kwargs):
    '''Detalle de agente.'''
    
    info_agente = info_header_agente(request)
    id_agente = info_agente.id
    
    itemObj = Agent_Model.objects.get(id=id_agente) 
    agente_inmuebles = Realstate_Model.objects.filter(fk_agent=id_agente).order_by('-date')
    agente_articulos = Article_Model.objects.filter(fk_agent=id_agente).order_by('-date')
    
    info_agente = info_header_agente(request)

    context = {
        'page' : 'Perfil de agente',
        'icon' : 'bx bxs-user-rectangle',
        'info_agente': info_agente,
        'singular' : 'agente',
        'plural' : 'agentes',
        'url_editar' : 'modificar_agente',
        'agente_inmuebles': agente_inmuebles,
        'agente_articulos': agente_articulos,
        'item': itemObj
    }
    return render(request, 'panel/ver_perfil.html', context)



@login_required(login_url='entrar')
def editar_perfil(request, *args, **kwargs):
    '''Editar agente.'''
    
    info_agente = info_header_agente(request)
    id_agente = info_agente.id
    
    itemObj = Agent_Model.objects.get(id=id_agente) 
    form = Agent_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Agent_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('ver_perfil')  
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



#=======================================================================================================================================
# Vistas para Páginas
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_paginas(request, *args, **kwargs):
    '''Lista páginas.'''
    
    object_list = Page_Model.objects.all() # Lista de objetos
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
        'page' : 'Páginas',
        'icon' : 'bx bxs-file',
        'info_agente': info_agente,
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'listar_paginas',
        'url_crear' : 'crear_pagina',
        'url_ver' : 'ver_pagina',
        'url_editar' : 'modificar_pagina',
        'url_eliminar' : 'eliminar_pagina',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


@login_required(login_url='entrar')
def ver_pagina(request, id, *args, **kwargs):
    '''Detalle de página.'''
    
    itemObj = Page_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Detalle de página',
        'icon' : 'bx bxs-file',
        'info_agente': info_agente,
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


@login_required(login_url='entrar')
def crear_pagina(request, *args, **kwargs):
    '''Crear página.'''
    
    form = Page_Form()
    
    if request.method == 'POST':
        form = Page_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            base_url = reverse('listar_paginas')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            #return redirect('listar_paginas')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Crear página',
        'icon' : 'bx bxs-file',
        'info_agente': info_agente,
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


@login_required(login_url='entrar')
def modificar_pagina(request, id, *args, **kwargs):
    '''Editar página.'''
    
    itemObj = Page_Model.objects.get(id=id) 
    form = Page_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Page_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            base_url = reverse('listar_paginas')  
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            #return redirect('listar_paginas')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Editar página',
        'icon' : 'bx bxs-file',
        'info_agente': info_agente,
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


@login_required(login_url='entrar')
def eliminar_pagina(request, id, *args, **kwargs):
    '''Eliminar página.'''
    
    itemObj = Page_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_paginas')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_paginas')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Eliminar página',
        'icon' : 'bx bxs-file',
        'info_agente': info_agente,
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
# Vistas para Mensajes de sección de contacto
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_mensajes_contacto(request, *args, **kwargs):
    '''Lista mensajes.'''
    
    object_list = Message_Contact_Model.objects.all() # Lista de objetos
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
        'page' : 'Mensajes de Contacto',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_contacto',
        'url_crear' : 'crear_mensaje_contacto',
        'url_ver' : 'ver_mensaje_contacto',
        'url_editar' : 'modificar_mensaje_contacto',
        'url_eliminar' : 'eliminar_mensaje_contacto',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_mini.html', context)


@login_required(login_url='entrar')
def ver_mensaje_contacto(request, id, *args, **kwargs):
    '''Detalle de mensaje.'''
    
    itemObj = Message_Contact_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Detalle de Mensajes de Contacto',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_contacto',
        'url_crear' : 'crear_mensaje_contacto',
        'url_ver' : 'ver_mensaje_contacto',
        'url_editar' : 'modificar_mensaje_contacto',
        'url_eliminar' : 'eliminar_mensaje_contacto',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail_mini.html', context)


@login_required(login_url='entrar')
def eliminar_mensaje_contacto(request, id, *args, **kwargs):
    '''Eliminar mensaje.'''
    
    itemObj = Message_Contact_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_mensajes_contacto')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_mensajes')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Eliminar Mensajes de Contacto',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_contacto',
        'url_crear' : 'crear_mensaje_contacto',
        'url_ver' : 'ver_mensaje_contacto',
        'url_editar' : 'modificar_mensaje_contacto',
        'url_eliminar' : 'eliminar_mensaje_contacto',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
    



#=======================================================================================================================================
# Vistas para Mensajes de inmuebles
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_mensajes_inmueble(request, *args, **kwargs):
    '''Lista mensajes.'''
    
    object_list = Message_Realstate_Model.objects.all() # Lista de objetos
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
        'page' : 'Mensajes de Contacto de Propiedades',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_inmueble',
        'url_ver' : 'ver_mensaje_inmueble',
        'url_eliminar' : 'eliminar_mensaje_inmueble',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_mini.html', context)


@login_required(login_url='entrar')
def ver_mensaje_inmueble(request, id, *args, **kwargs):
    '''Detalle de mensaje.'''
    
    itemObj = Message_Realstate_Model.objects.get(id=id) 
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Detalle de Mensaje de Propiedad',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_inmueble',
        'url_ver' : 'ver_mensaje_inmueble',
        'url_eliminar' : 'eliminar_mensaje_inmueble',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail_mini.html', context)


@login_required(login_url='entrar')
def eliminar_mensaje_inmueble(request, id, *args, **kwargs):
    '''Eliminar mensaje.'''
    
    itemObj = Message_Realstate_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_mensajes_inmueble')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_mensajes')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Eliminar Mensajes de Propiedad',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_inmueble',
        'url_ver' : 'ver_mensaje_inmueble',
        'url_eliminar' : 'eliminar_mensaje_inmueble',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Mensajes de Agentes
#=======================================================================================================================================

@login_required(login_url='entrar')
def listar_mensajes_agente(request, *args, **kwargs):
    '''Lista mensajes.'''
    
    object_list = Message_Agent_Model.objects.all() # Lista de objetos
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
        'page' : 'Mensajes de Contacto de Agente',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_agente',
        'url_crear' : 'crear_mensaje_agente',
        'url_ver' : 'ver_mensaje_agente',
        'url_eliminar' : 'eliminar_mensaje_agente',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_noedit.html', context)


@login_required(login_url='entrar')
def ver_mensaje_agente(request, id, *args, **kwargs):
    '''Detalle de mensaje.'''
    
    itemObj = Message_Agent_Model.objects.get(id=id) 
    
    agente_actual = request.user.id
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Detalle de Mensajes de Agente',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_agente',
        'url_crear' : 'crear_mensaje_agente',
        'url_ver' : 'ver_mensaje_agente',
        'url_eliminar' : 'eliminar_mensaje_agente',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail_mini.html', context)


@login_required(login_url='entrar')
def crear_mensaje_agente(request, *args, **kwargs):
    '''Crear mensaje.'''
    
    info_agente = info_header_agente(request)
    print(f'agent_sender: {info_agente.id}')
    
    form = Message_Agent_Form()
    
    if request.method == 'POST':
        form = Message_Agent_Form(request.POST, request.FILES)
        if form.is_valid():
            
            form.agent_sender = info_agente.id
            form.save()
            
            base_url = reverse('listar_mensajes_agente')  
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 

    
    form = Message_Agent_Form(initial={
        'agent_sender': info_agente.id, 
    })
    
    context = {
        'page' : 'Crear Mensaje de Agente',
        'icon' : 'bx bxs-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_agente',
        'url_crear' : 'crear_mensaje_agente',
        'url_ver' : 'ver_mensaje_agente',
        'url_eliminar' : 'eliminar_mensaje_agente',
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)


@login_required(login_url='entrar')
def eliminar_mensaje_agente(request, id, *args, **kwargs):
    '''Eliminar mensaje.'''
    
    itemObj = Message_Agent_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_mensajes_agente')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_mensajes')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Eliminar Mensajes de Agente',
        'icon' : 'bx bx-file',
        'info_agente': info_agente,
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'listar_mensajes_agente',
        'url_crear' : 'crear_mensaje_agente',
        'url_ver' : 'ver_mensaje_agente',
        'url_eliminar' : 'eliminar_mensaje_agente',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)




#=======================================================================================================================================
# Vistas para Búsquedas
#=======================================================================================================================================

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_busquedas_frontend(request, *args, **kwargs):
    '''Lista búsquedas.'''
    
    object_list = Frontend_Search_Model.objects.all() # Lista de objetos
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
        'page' : 'Búsquedas de artículos en el sitio web',
        'singular' : 'búsqueda',
        'info_agente': info_agente,
        'plural' : 'búsquedas',
        'url_activo_index' : 'listar_busquedas_frontend',
        'url_eliminar' : 'eliminar_busqueda_frontend',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_search.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_busquedas_backend(request, *args, **kwargs):
    '''Lista búsquedas.'''
    
    object_list = Backend_Search_Model.objects.all() # Lista de objetos
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
        'page' : 'Búsquedas de panel de administración',
        'singular' : 'búsqueda',
        'info_agente': info_agente,
        'plural' : 'búsquedas',
        'url_activo_index' : 'listar_busquedas_backend',
        'url_eliminar' : 'eliminar_busqueda_backend',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_delete': success_delete,
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_search.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def eliminar_busqueda_frontend(request, id, *args, **kwargs):
    '''Eliminar búsqueda.'''
    
    itemObj = Frontend_Search_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_busquedas_frontend')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_busquedas_frontend')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Eliminar búsqueda de sitio web',
        'singular' : 'búsqueda',
        'info_agente': info_agente,
        'plural' : 'búsquedas',
        'url_activo_index' : 'listar_busquedas_frontend',
        'url_eliminar' : 'eliminar_busqueda_frontend',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def eliminar_busqueda_backend(request, id, *args, **kwargs):
    '''Eliminar búsqueda.'''
    
    itemObj = Backend_Search_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        base_url = reverse('listar_busquedas_backend')  
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        # return redirect('listar_busquedas_backend')

    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Eliminar búsqueda de panel de administración',
        'singular' : 'búsqueda',
        'info_agente': info_agente,
        'plural' : 'búsquedas',
        'url_activo_index' : 'listar_busquedas_backend',
        'url_eliminar' : 'eliminar_busqueda_backend',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)


#=======================================================================================================================================

@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def blank(request, *args, **kwargs):
    '''Test'''
    
    info_agente = info_header_agente(request)
    
    context = {
        'page' : 'Blank',
        'info_agente': info_agente,
    }
    return render(request, 'panel/blank.html', context)

