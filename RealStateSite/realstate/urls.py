from django.urls import path
import realstate.views

urlpatterns = [

#realstate 
    path('inmuebles/', realstate.views.listar_inmuebles, name='listar_inmuebles'),
    path('inmuebles/<int:id>/', realstate.views.ver_inmueble, name='ver_inmueble'),
    path('inmuebles/crear/', realstate.views.crear_inmueble, name='crear_inmueble'),
    path('inmuebles/modificar/<int:id>/', realstate.views.modificar_inmueble, name='modificar_inmueble'),
    path('inmuebles/eliminar/<int:id>/', realstate.views.eliminar_inmueble, name='eliminar_inmueble'),
    
#realstate_type
    path('tipo_inmuebles/', realstate.views.listar_tipo_inmuebles, name='listar_tipo_inmuebles'),
    path('tipo_inmuebles/<int:id>/', realstate.views.ver_tipo_inmueble, name='ver_tipo_inmueble'),
    path('tipo_inmuebles/crear/', realstate.views.crear_tipo_inmueble, name='crear_tipo_inmueble'),
    path('tipo_inmuebles/modificar/<int:id>/', realstate.views.modificar_tipo_inmueble, name='modificar_tipo_inmueble'),
    path('tipo_inmuebles/eliminar/<int:id>/', realstate.views.eliminar_tipo_inmueble, name='eliminar_tipo_inmueble'),

]