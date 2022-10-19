from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from realstate.models import Realstate_Model, Message_Realstate_Model
from panel.models import Message_Contact_Model, Frontend_Search_Model

#=======================================================================================================================================
# Propiedades
#=======================================================================================================================================

class addpropertyform(forms.Form):
    address = forms.CharField(max_length=50)
    location =forms.CharField(max_length=50)
    price = forms.IntegerField()



#=======================================================================================================================================
# Funcionalidades del sitio 
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
            'fk_agent',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Message_Realstate_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            
        self.fields['fk_agent'].widget = forms.HiddenInput()



class Message_Contact_Form(ModelForm):
    class Meta:
        model = Message_Contact_Model
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Message_Contact_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            
            
            
class Frontend_Article_Search_Form(ModelForm):
    class Meta:
        model = Frontend_Search_Model
        fields = [
            'name',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Frontend_Article_Search_Form, self).__init__(*args, **kwargs)


class Frontend_Realstate_Search_Form(ModelForm):
    class Meta:
        model = Frontend_Search_Model
        fields = [
            'name',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Frontend_Article_Search_Form, self).__init__(*args, **kwargs)
    
    