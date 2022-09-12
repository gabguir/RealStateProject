from django.urls import path
from django.views.i18n import JavaScriptCatalog
import panel.views


urlpatterns = [

#index
    path('', panel.views.app_panel_index, name='app_panel_index'),
    path('resultados_busqueda/', panel.views.resultados_busqueda, name='resultados_busqueda'),
    path('listar_busquedas/', panel.views.listar_busquedas, name='listar_busquedas'),
    path('eliminar_busqueda/', panel.views.eliminar_busqueda, name='eliminar_busqueda'),

#inmueble 
    path('listar_inmuebles/', panel.views.listar_inmuebles, name='listar_inmuebles'),
    path('crear_inmueble/', panel.views.crear_inmueble, name='crear_inmueble'),
    path('ver_inmueble/<int:id>/', panel.views.ver_inmueble, name='ver_inmueble'),
    path('modificar_inmueble/<int:id>/', panel.views.modificar_inmueble, name='modificar_inmueble'),
    path('eliminar_inmueble/<int:id>/', panel.views.eliminar_inmueble, name='eliminar_inmueble'),

#agentes 
    path('listar_agentes/', panel.views.listar_agentes, name='listar_agentes'),
    path('crear_agente/', panel.views.crear_agente, name='crear_agente'),
    path('ver_agente/<int:id>/', panel.views.ver_agente, name='ver_agente'),
    path('modificar_agente/<int:id>/', panel.views.modificar_agente, name='modificar_agente'),
    path('eliminar_agente/<int:id>/', panel.views.eliminar_agente, name='eliminar_agente'),

#clientes  
    path('listar_clientes/', panel.views.listar_clientes, name='listar_clientes'),
    path('crear_cliente/', panel.views.crear_cliente, name='crear_cliente'),
    path('ver_cliente/<int:id>/', panel.views.ver_cliente, name='ver_cliente'),
    path('modificar_cliente/<int:id>/', panel.views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:id>/', panel.views.eliminar_cliente, name='eliminar_cliente'),

#paginas
    path('listar_paginas/', panel.views.listar_paginas, name='listar_paginas'),
    path('crear_pagina/', panel.views.crear_pagina, name='crear_pagina'),
    path('ver_pagina/<int:id>/', panel.views.ver_pagina, name='ver_pagina'),
    path('modificar_pagina/<int:id>/', panel.views.modificar_pagina, name='modificar_pagina'),
    path('eliminar_pagina/<int:id>/', panel.views.eliminar_pagina, name='eliminar_pagina'),

#articulos
    path('listar_articulos/', panel.views.listar_articulos, name='listar_articulos'),
    path('ver_articulo/<int:id>/', panel.views.ver_articulo, name='ver_articulo'),
    path('crear_articulo/', panel.views.crear_articulo, name='crear_articulo'),
    path('modificar_articulo/<int:id>/', panel.views.modificar_articulo, name='modificar_articulo'),
    path('eliminar_articulo/<int:id>/', panel.views.eliminar_articulo, name='eliminar_articulo'),

#categoria
    path('listar_categorias/', panel.views.listar_categorias, name='listar_categorias'),
    path('crear_categoria/', panel.views.crear_categoria, name='crear_categoria'),
    path('ver_categoria/<int:id>/', panel.views.ver_categoria, name='ver_categoria'),
    path('modificar_categoria/<int:id>/', panel.views.modificar_categoria, name='modificar_categoria'),
    path('eliminar_categoria/<int:id>/', panel.views.eliminar_categoria, name='eliminar_categoria'),

#imagenes
    path('listar_imagenes/', panel.views.listar_imagenes, name='listar_imagenes'),
    path('crear_imagen/', panel.views.crear_imagen, name='crear_imagen'),
    path('ver_imagen/<int:id>/', panel.views.ver_imagen, name='ver_imagen'),
    path('modificar_imagen/<int:id>/', panel.views.modificar_imagen, name='modificar_imagen'),
    path('eliminar_imagen/<int:id>/', panel.views.eliminar_imagen, name='eliminar_imagen'),

    #JS-Catalog para mostrar widget admin para fechas y horas
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),

]