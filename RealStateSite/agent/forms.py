from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from agent.models import Agent_Model

#=======================================================================================================================================
# Agent
#=======================================================================================================================================

class Agent_Form(ModelForm):
    class Meta:
        model = Agent_Model
        fields = [
            'name',
            'email',
            'image_main',
            'description',
            
            'url_twitter',
            'url_facebook',
            'url_linkedin',
            'url_instagram',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Agent_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
