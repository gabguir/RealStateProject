from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from blog.models import Article_Model, Category_Model
from agent.models import Agent_Model


#=======================================================================================================================================
# Article 
#=======================================================================================================================================

class Article_Form(ModelForm):
    date = forms.DateField(
        widget=AdminDateWidget()
    )

    class Meta:
        model = Article_Model
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            'content',
            'date',
            'fk_categoria',
            'fk_agent',
            
            'image_main',
            'image_01',
            'image_02',
            'image_03',
            'image_04',
            'image_05',
            
            'draft',
        ]

    def __init__(self, *args, **kwargs):
        super(Article_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['subtitle'].widget.attrs.update({'class':'form-control'})
        self.fields['abstract'].widget.attrs.update({'class':'form-control'})
        self.fields['content'].widget.attrs.update({'class':'form-control'})
        #date
        self.fields['image_main'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_01'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_02'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_03'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_04'].widget.attrs.update({'class':'form-control-file'})
        self.fields['image_05'].widget.attrs.update({'class':'form-control-file'})
        
        self.fields['draft'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_categoria'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_agent'].widget.attrs.update({'class':'form-control'})




#=======================================================================================================================================
# Category 
#=======================================================================================================================================

class Category_Form(ModelForm):
    class Meta:
        model = Category_Model
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(Category_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



#=======================================================================================================================================
# Image
#=======================================================================================================================================

# class Image_Article_Form(ModelForm):
#     class Meta:
#         model = Image_Article_Model
#         fields = [
#             'name',
#             'pic',
#         ]
#     def __init__(self, *args, **kwargs):
#         super(Image_Article_Form, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class':'form-control'})
