from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from django.db.models import Q

# Importar models desde apps de backend
from panel.models import Page_Model, Backend_Search_Model, Frontend_Search_Model, Message_Model
from agent.models import Agent_Model
from blog.models import Article_Model, Category_Model
from customer.models import Customer_Model
from realstate.models import Realstate_Model, Realstate_Type_Model

# Importar forms desde apps de backend
from website.forms import Message_Form, Frontend_Article_Search_Form, Frontend_Realstate_Search_Form


#=======================================================================================================================================
# Páginas del sitio
#=======================================================================================================================================

def home(request):
    page_content = Page_Model.objects.filter(name='inicio')
    agent_content = Page_Model.objects.filter(name='agents')
    agentes_list = Agent_Model.objects.all()[:3]
    inmuebles_list = Realstate_Model.objects.filter(draft=False).order_by('-date')[:3] 
    articulos_list = Article_Model.objects.filter(draft=False).order_by('-date')[:3] 
    
    context = {
        'page' : 'Inicio',
        'page_content': page_content,
        'agent_content': agent_content,
        'agentes': agentes_list,
        'inmuebles': inmuebles_list,
        'articulos': articulos_list,
    }
    
    return render(request, "website/inicio.html", context)


def agents(request):
    page_content = Page_Model.objects.filter(name='agents')
    agentes_list = Agent_Model.objects.all() 

    context = {
        'page' : 'Agentes',
        'page_content': page_content,
        'agentes': agentes_list,
    }
    return render(request, "website/agents.html", context)


def about(request):
    page_content = Page_Model.objects.filter(name='about')
    context = {
        'page' : 'Nosotros',
        'page_content': page_content
    }
    return render(request, "website/about.html", context)



def contact(request):
    page_content = Page_Model.objects.filter(name='contact')
    
    '''Crear mensaje.'''
    form = Message_Form()
    error_message = ''
    success_message = ''
    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name = info['name']
            email = info['email']
            subject = info['subject']
            message = info['message']
            
            mensaje = Message_Model(
                name = name, 
                email = email,
                subject = subject,
                message = message,
            )

            mensaje.save()
            #return redirect('app_blog_index')
            success_message = 'OK'
            #mensaje exitoso
        
        else:
            #mensaje invalido
            print("form invalido")
            error_message = 'ERROR'
            
    context = {
        'page' : 'Contacto',
        'page_content' : page_content,
        'success_message' : success_message,
        'error_message' : error_message,
    }
    return render(request, "website/contact.html", context)



#=======================================================================================================================================
# Blog
#=======================================================================================================================================


def blog(request):
    page_content = Page_Model.objects.filter(name='blog')
    articulos_list = Article_Model.objects.filter(draft=False).order_by('-date') 
    context = {
        'page' : 'Blog',
        'page_content': page_content,
        'articulos': articulos_list,
    }
    
    return render(request, "website/blog.html", context)


def blog_detail(request, id):
    itemObj = Article_Model.objects.get(id=id) 
    print(itemObj)
    context = {
        'page' : 'Blog',
        'articulo': itemObj,
    }
    
    return render(request, "website/blog_detail.html", context)



#=======================================================================================================================================
# Inmuebles
#=======================================================================================================================================


def realstates(request):
    page_content = Page_Model.objects.filter(name='realstates')
    inmuebles_list = Realstate_Model.objects.filter(draft=False).order_by('-date')
    
    context = {
        'page' : 'Propiedades',
        'page_content': page_content,
        'inmuebles': inmuebles_list,
    }
    
    return render(request, "website/properties.html", context)


def realstates_detail(request, id):
    itemObj = Realstate_Model.objects.get(id=id) 
    # print(itemObj)
    context = {
        'page' : 'Propiedades',
        'inmueble': itemObj,
    }
    
    return render(request, "website/property_detail.html", context)



def addproperty(request):
    if request.method=="POST":
        form= addpropertyform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            address= info["address"]
            location= info["location"]
            price= info["price"]
            realstate= Realstate_Model(address=address, location=location, price=price)
            realstate.save()
            return render (request, "website/savedtodatabase.html", {"message":"Property created"})
    else:
        form= addpropertyform()
    return render(request, "website/addproperty.html", {"form":form})



#=======================================================================================================================================
# Funcionalidades: Buscador y mensajes
#=======================================================================================================================================

# def search_old(request):
#     if request.method=="POST":
#         location = request.POST['location']
#         #Search for all properties on specified location
#         realstate = Realstate_Model.objects.filter(location__contains=location)
#         print(f"realstate: {realstate}")
#         return render(request, "website/searchresult.html", {"location":location, "realstate":realstate})
#     else:
#         return render(request, "website/inicio.html", {"message":"Ingrese una ciudad."})
    
#     return HttpResponse(response)



def resultados_busqueda_inmuebles(request, *args, **kwargs):
    '''Muestra resultados de búsqueda.'''
    page_content = Page_Model.objects.filter(name='search_result')
    form = Frontend_Realstate_Search_Form()
    vacio = True
    termino_busqueda = ''
    result_realstate = ''
    
    if request.method == 'POST':
        form = Frontend_Realstate_Search_Form(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['name']
            print(termino_busqueda)
            #form.save()

        if termino_busqueda == '':
            vacio = True
        else:
            vacio = False
            result_realstate = Realstate_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(address__icontains=termino_busqueda) |
                Q(location__icontains=termino_busqueda)
                ).filter(draft=False).order_by('date')

    context = {
        'page': 'Resultados de búsqueda',
        'page_content': page_content,
        'termino_busqueda': termino_busqueda,
        'vacio': vacio,
        'inmuebles': result_realstate,
        'paginas': page_content,
    }
    return render(request, 'website/realstate_search_result.html', context)


def resultados_busqueda_articulos(request, *args, **kwargs):
    '''Muestra resultados de búsqueda.'''
    
    form = Frontend_Article_Search_Form()
    vacio = True
    termino_busqueda = ''
    result_articulo = ''
    
    if request.method == 'POST':
        form = Frontend_Article_Search_Form(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['name']
            print(termino_busqueda)
            form.save()

        if termino_busqueda == '':
            vacio = True
        else:
            vacio = False
            result_articulo = Article_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(title__icontains=termino_busqueda) |
                Q(subtitle__icontains=termino_busqueda) |
                Q(abstract__icontains=termino_busqueda) |
                Q(content__icontains=termino_busqueda)
                ).filter(draft=False).order_by('date')

    page_content = Page_Model.objects.all() # Lista de paginas
    
    context = {
        'page': 'Resultados de búsqueda',
        'termino_busqueda': termino_busqueda,
        'vacio': vacio,
        'result_articulo': result_articulo,
        'paginas': page_content,
    }
    return render(request, 'website/resultados_busqueda.html', context)
