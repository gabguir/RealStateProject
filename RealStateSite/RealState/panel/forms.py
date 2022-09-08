from django.forms import ModelForm
from django import forms
from Main.models import Property, Agent, Customer
from Main.models import Page, Article, Category, Image


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
        
        
class Customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'email',
        ]

class Page_Form(ModelForm):
    class Meta:
        model = Page
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            #'date',
            'content',
            #'draft',
        ]



class Article_Form(ModelForm):
    class Meta:
        model = Article
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            #'date',
            'content',
            'draft',
            'fk_categoria',
        ]



class Category_Form(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]



class Image_Form(ModelForm):
    class Meta:
        model = Image
        fields = [
            'name',
            'pic',
            #'date',
        ]


