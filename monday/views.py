from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def About_page(req):
    return HttpResponse("Hellow World")
    
def Home(req):
    return JsonResponse({"checking Status":"complated"})
# html templated

def showLanding_html(req):
    return render(req, "home.html")

def properties(req):
    return render(req, "properties.html")

def property_details(req):
    return render(req, "property-details.html")

def contact(req):
    return render(req, "contact.html")