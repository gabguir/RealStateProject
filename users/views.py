from django.shortcuts import render

# Create your views here.



def profiles(request, *args, **kwargs):
    '''Usuarios'''
    
    context = {
        'page' : 'Usuarios',
    }
    return render(request, 'users/profiles.html', context)



