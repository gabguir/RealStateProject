from django import forms

class addpropertyform(forms.Form):
    address = forms.CharField(max_length=50)
    location =forms.CharField(max_length=50)
    price = forms.IntegerField()



    