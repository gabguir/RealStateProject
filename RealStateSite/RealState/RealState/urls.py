"""RealState URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="base"),
    path('inicio', home, name="inicio"),
    path('agents/', agents, name="agents"),
    path('about/', about, name="about"),
    path('addproperty/', addproperty, name="addproperty"),
    path('search/', search, name="search"),
    
    # inclusión de urls de panel
    path('panel/', include('panel.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
