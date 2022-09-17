from django.urls import path
import customer.views

urlpatterns = [

#customer  
    path('clientes/', customer.views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:id>/', customer.views.ver_cliente, name='ver_cliente'),
    path('clientes/crear/', customer.views.crear_cliente, name='crear_cliente'),
    path('clientes/modificar/<int:id>/', customer.views.modificar_cliente, name='modificar_cliente'),
    path('clientes/eliminar/<int:id>/', customer.views.eliminar_cliente, name='eliminar_cliente'),

]