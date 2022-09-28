from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from realstate.models import Realstate_Model, Realstate_Type_Model, Message_Realstate_Model
from agent.models import Agent_Model

#=======================================================================================================================================
# Realstate_Model 
#=======================================================================================================================================

class Realstate_Form(ModelForm):
    date = forms.DateField(
        widget=AdminDateWidget()
    )
    
    class Meta:
        model = Realstate_Model
        fields = [
            'name',
            'address',
            'price',
            'location',
            'fk_tipo_inmueble',
            'fk_agent',
            'bath_qty',
            'room_qty',
            'date',
            'description',
            
            'image_main',
            'image_01',
            'image_02',
            'image_03',
            'image_04',
            'image_05',
            
            'draft',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Realstate_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        self.fields['price'].widget.attrs.update({'class':'form-control'})
        self.fields['location'].widget.attrs.update({'class':'form-control'})
        self.fields['bath_qty'].widget.attrs.update({'class':'form-control'})
        self.fields['room_qty'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        #date
        self.fields['image_main'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_01'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_02'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_03'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_04'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_05'].widget.attrs.update({'class':'form-control-file'})
        
        self.fields['draft'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_tipo_inmueble'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_agent'].widget.attrs.update({'class':'form-control'})

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})


#=======================================================================================================================================
# Realstate_Type_Model 
#=======================================================================================================================================

class Realstate_Type_Form(ModelForm):
    class Meta:
        model = Realstate_Type_Model
        fields = [
            'name',
            'description',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Realstate_Type_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


#=======================================================================================================================================
# Message_Realstate_Model 
#=======================================================================================================================================

class Message_Realstate_Form(ModelForm):
    class Meta:
        model = Message_Realstate_Model
        fields = [
            'name',
            'email',
            'subject',
            'message',
            'fk_realstate',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Message_Realstate_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

