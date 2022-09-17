from django.urls import path
import agent.views

urlpatterns = [

#agent 
    path('agentes/', agent.views.listar_agentes, name='listar_agentes'),
    path('agentes/<int:id>/', agent.views.ver_agente, name='ver_agente'),
    path('agentes/crear/', agent.views.crear_agente, name='crear_agente'),
    path('agentes/editar/<int:id>/', agent.views.modificar_agente, name='modificar_agente'),
    path('agente/eliminar/<int:id>/', agent.views.eliminar_agente, name='eliminar_agente'),

]