from agent.models import Agent_Model

#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

def info_header_agente(request, *args, **kwargs):
    
    if request.user.groups.filter(name='admin').exists():
        return Agent_Model.objects.get(user=request.user.id)
    elif request.user.groups.filter(name='agent').exists():
        return Agent_Model.objects.get(user=request.user.id)
