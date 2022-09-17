from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from panel.models import Page_Model, Frontend_Search_Model, Backend_Search_Model, Message_Model



#=======================================================================================================================================
# Page
#=======================================================================================================================================

class Page_Form(ModelForm):
    date = forms.DateField(
        widget=AdminDateWidget()
    )

    class Meta:
        model = Page_Model
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            'content',
            'date',
            'image_main',
        ]

    def __init__(self, *args, **kwargs):
        super(Page_Form, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['subtitle'].widget.attrs.update({'class':'form-control'})
        self.fields['abstract'].widget.attrs.update({'class':'form-control'})
        self.fields['content'].widget.attrs.update({'class':'form-control'})
        #date
        self.fields['image_main'].widget.attrs.update({'class':'form-control-file'})
        

#=======================================================================================================================================
# Message 
#=======================================================================================================================================

class Message_Form(ModelForm):
    class Meta:
        model = Message_Model
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Message_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            
            
            
#=======================================================================================================================================
# Frontend_Search 
#=======================================================================================================================================

class Frontend_Search_Form(ModelForm):
    class Meta:
        model = Frontend_Search_Model
        fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):
        super(Frontend_Search_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



#=======================================================================================================================================
# Backend_Search 
#=======================================================================================================================================

class Backend_Search_Form(ModelForm):
    class Meta:
        model = Backend_Search_Model
        fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):
        super(Backend_Search_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
