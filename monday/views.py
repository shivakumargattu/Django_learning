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
    