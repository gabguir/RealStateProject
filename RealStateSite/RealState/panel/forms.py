from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from Main.models import Property, Agent, Customer
from Main.models import Page, Article, Category, Image
from panel.models import Search


#=======================================================================================================================================
# Forms 
#=======================================================================================================================================

class Property_Form(ModelForm):
    class Meta:
        model = Property
        fields = [
            'name',
            'address',
            'price',
            'location',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Property_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        
        
class Agent_Form(ModelForm):
    class Meta:
        model = Agent
        fields = [
            'name',
            'email',
            'image',
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
        
        
class Customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'email',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Customer_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class Page_Form(ModelForm):
    abstract = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    class Meta:
        model = Page
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            #'date',
            'content',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
            'title': forms.TextInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
            'subtitle': forms.TextInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
        }
    def __init__(self, *args, **kwargs):
        super(Page_Form, self).__init__(*args, **kwargs)



class Article_Form(ModelForm):
    date = forms.DateField(
        widget=AdminDateWidget()
        #input_formats=["%Y-%m-%d"],
        # widget=forms.DateInput(attrs={
        #     "class": "form-control datetimepicker-input",
        #     "data-target": "#datetimepicker1"
        # })
    )
    abstract = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": ""
            }
        )
    )
        
    class Meta:
        model = Article
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            'date',
            'content',
            'image',
            'draft',
            'fk_categoria',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
            'title': forms.TextInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
            'subtitle': forms.TextInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
            'date': forms.DateInput(attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker1"
            }),
            'draft': forms.CheckboxInput(attrs={
                "class": "form-check",
                #"placeholder": ""
            }),
            'image': forms.FileInput(attrs={
                "class": "form-control",
                #"placeholder": ""
            }),
        }
    def __init__(self, *args, **kwargs):
        super(Article_Form, self).__init__(*args, **kwargs)
        
        self.fields['fk_categoria'].widget.attrs.update(
            {'class': 'custom-select', 'placeholder': ''})



class Category_Form(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(Category_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class Image_Form(ModelForm):
    class Meta:
        model = Image
        fields = [
            'name',
            'pic',
        ]
    def __init__(self, *args, **kwargs):
        super(Image_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class Search_Form(ModelForm):
    class Meta:
        model = Search
        fields = [
            'name',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Search_Form, self).__init__(*args, **kwargs)
