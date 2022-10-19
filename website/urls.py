from django.urls import path, include
from django.conf.urls.static import static
from website.views import *

urlpatterns = [

    #páginas
    path('', home, name="inicio"),
    path('agentes/', agents, name="agents"),
    path('agentes/<int:id>', agents_detail, name="agents_detail"),
    path('nosotros/', about, name="about"),
    path('contacto/', contact, name="contact"),
    
    #artículos
    path('blog/', blog, name="blog"),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    
    #inmuebles
    path('propiedades/', realstates, name="realstates"),
    path('propiedades/<int:id>/', realstates_detail, name="realstates_detail"),
    
    # otras urls
    #path('addproperty/', addproperty, name="addproperty"),
    #path('search/', search, name="search"),
    path('resultado_busqueda/', resultados_busqueda_inmuebles, name="resultados_busqueda_inmuebles"),

]