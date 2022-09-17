from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from customer.models import Customer_Model


#=======================================================================================================================================
# Customer 
#=======================================================================================================================================

class Customer_Form(ModelForm):
    class Meta:
        model = Customer_Model
        fields = [
            'name',
            'email',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Customer_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
