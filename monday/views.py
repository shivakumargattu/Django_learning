from django.http import HttpResponse
from django.http import JsonResponse

def About_page(req):
    return HttpResponse("Hellow World")
    
def Home(req):
    return JsonResponse({"checking Status":"complated"})