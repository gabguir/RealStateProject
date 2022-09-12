from django.shortcuts import render
from django.http import HttpResponse
from Main.models import *
from Main.forms import *
# Create your views here.

def home(request):
    return render(request, "RealStateApp/inicio.html")


def agents(request):
    content = Page.objects.get(name='agents')
    queryset = Agent.objects.all() # Lista de objetos
    context = {
        'page' : 'Agentes',
        'content': content,
        'agentes': queryset
    }
    return render(request, "RealStateApp/agents.html", context)


def about(request):
    content = Page.objects.get(name='about')
    context = {
        'page' : 'About',
        'content': content
    }
    return render(request, "RealStateApp/about.html", context)

def blog(request):
    return render(request, "RealStateApp/blog.html")


def blog_detail(request):
    return render(request, "RealStateApp/blog_detail.html")


def addproperty(request):
    if request.method=="POST":
        form= addpropertyform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            address= info["address"]
            location= info["location"]
            price= info["price"]
            property= Property(address=address, location=location, price=price)
            property.save()
            return render (request, "RealStateApp/savedtodatabase.html", {"message":"Property created"})
    else:
        form= addpropertyform()
    return render(request, "RealStateApp/addproperty.html", {"form":form})


def search(request):
    if request.method=="POST":
        location = request.POST['location']
        #Search for all properties on specified location
        property=Property.objects.filter(location__contains=location)
        print(f"{property}")
        return render(request, "RealStateApp/searchresult.html", {"location":location, "property":property})
    else:
        return render(request, "RealStateApp/inicio.html", {"message":"Enter Location"})
    
    return HttpResponse(response)
