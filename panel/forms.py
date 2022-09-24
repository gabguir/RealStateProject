from django.forms import ModelForm
from django import forms
from django.forms import ModelForm, Textarea, CheckboxInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
import datetime

# importaciones para usuarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Importación de modelos
from panel.models import Page_Model, Frontend_Search_Model, Backend_Search_Model, Message_Contact_Model



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


#=======================================================================================================================================
# Login 
#=======================================================================================================================================


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese el usuario...'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingrese el password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirme el password...'})

