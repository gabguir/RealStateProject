from django.http import HttpResponse
from django.shortcuts import render, redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app_panel_index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            # print('Working: ', allowed_roles)
            group = None
            if request.user.groups.exists():
                # recupera el nombre del primer grupo de usuarios
                # donde está este usuario
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else: 
                #return HttpResponse('Sin autorización para ver esta página.')
                return render(request, 'login/404.html')

        return wrapper_func
    return decorator

    # Grupos de usuarios
    # admin
    # agente
