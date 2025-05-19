from django.http import HttpResponse

def About_page(req):
    return HttpResponse("Hellow World")
    
def Home(req):
    return HttpResponse("Checking Completed")