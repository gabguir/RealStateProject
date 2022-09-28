from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog
import users.views



urlpatterns = [

#dashboard
    path('usuarios/', users.views.profiles, name='profiles'),
    


#=======================================================================================================================================
# Otras rutas
#=======================================================================================================================================

    #path('blank/', users.views.blank, name='blank'),

] # fin urlpatterns