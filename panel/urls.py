from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog
import panel.views


urlpatterns = [

#panel
    path('', panel.views.app_panel_index, name='app_panel_index'),
    path('resultados_busqueda/', panel.views.resultados_busqueda, name='resultados_busqueda'),

#buscar    
    path('busqueda_frontend/', panel.views.listar_busquedas_frontend, name='listar_busquedas_frontend'),
    path('busqueda_frontend/eliminar/<int:id>', panel.views.eliminar_busqueda_frontend, name='eliminar_busqueda_frontend'),
    path('busqueda_backend/', panel.views.listar_busquedas_backend, name='listar_busquedas_backend'),
    path('busqueda_backend/eliminar/<int:id>', panel.views.eliminar_busqueda_backend, name='eliminar_busqueda_backend'),

#page
    path('paginas/', panel.views.listar_paginas, name='listar_paginas'),
    path('paginas/<int:id>/', panel.views.ver_pagina, name='ver_pagina'),
    path('paginas/crear/', panel.views.crear_pagina, name='crear_pagina'),
    path('paginas/modificar/<int:id>/', panel.views.modificar_pagina, name='modificar_pagina'),
    path('paginas/eliminar/<int:id>/', panel.views.eliminar_pagina, name='eliminar_pagina'),

#message
    path('mensajes/', panel.views.listar_mensajes, name='listar_mensajes'),
    path('mensajes/<int:id>/', panel.views.ver_mensaje, name='ver_mensaje'),
    path('mensajes/eliminar/<int:id>/', panel.views.eliminar_mensaje, name='eliminar_mensaje'),

#JS-Catalog para mostrar widget admin para fechas y horas
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),

#=======================================================================================================================================
# Inclusiones 
#=======================================================================================================================================

#agent
    path('', include('agent.urls')),
    
#agent
    path('', include('blog.urls')),

#realstate 
    path('', include('realstate.urls')),

#customer 
    path('', include('customer.urls')),


#=======================================================================================================================================
# Login 
#=======================================================================================================================================

    path('test/', panel.views.test, name='test'),

    # path('login/', panel.views.login, name='inicio'),
    path('entrar/', panel.views.entrar, name='entrar'),
    # path('salir/', login.views.salir, name='salir'),
    # path('crear_usuario/', login.views.crear_usuario, name='crear_usuario'),

    # path('ver_perfil/', login.views.ver_perfil, name='ver_perfil'),
    # path('modificar_perfil/', login.views.modificar_perfil, name='modificar_perfil'),


#=======================================================================================================================================
# Reset de password
#=======================================================================================================================================

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),
        name='reset_password'),
    path('reset_password_enviado/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_sent.html'), 
        name='password_reset_done'),
    path('reset_password_confirmado/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_form.html'), 
        name='password_reset_confirm'),
    path('reset_password_completado/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_done.html'), 
        name='password_reset_complete'),




]