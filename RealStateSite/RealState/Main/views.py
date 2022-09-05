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
    if request.GET.get('location'):

        location=request.GET.get('location')
        #Search for all properties on specified location
        Property=property.objects.filter(location=location)
        return render(request, "RealStateApp/searchresult.html", {"Property":property.address,"Price":property.price, "Location":location})
    else:
        return render(request, "RealStateApp/base.html", {"message":"Enter Location"})
    
    return HttpResponse(response)
