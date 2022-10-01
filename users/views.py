from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from urllib.parse import urlencode

# importación de funcionalidad para login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
# importar custom decorators
from panel.decorators import authenticated_user, allowed_users

@login_required(login_url='entrar')
def profiles(request, *args, **kwargs):
    '''Usuarios'''
    
    context = {
        'page' : 'Usuarios',
    }
    return render(request, 'users/profiles.html', context)



