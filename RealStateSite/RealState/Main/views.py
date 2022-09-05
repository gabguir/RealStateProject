from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from Main.forms import *
# Create your views here.

def home(request):
    return render (request, "RealStateApp/base.html")

def agents(request):
    return render

def about(request):
    return render

def addproperty(request):

    if request.method=="POST":
        form= addpropertyform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            address= info["address"]
            location= info["location"]
            price= info["price"]
            Property= property(address=address, location=location, price=price)
            Property.save()
            return render (request, "RealStateApp/base.html", {"message":"Property created"})
    else:
        form= addpropertyform()
    return render(request, "RealStateApp/addproperty.html", {"form":form})

def search(request):

    if request.method=="POST":
        location = request.POST['location']
        #Search for all properties on specified location
        Property=property.objects.filter(location__contains=location)
        return render(request, "RealStateApp/searchresult.html", {"location":location, "property":property})
    else:
        return render(request, "RealStateApp/base.html", {"message":"Enter Location"})
    
    return HttpResponse(response)
