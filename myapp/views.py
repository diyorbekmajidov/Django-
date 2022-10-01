from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    a=request.POST
    r = JsonResponse({'sum':int(a.get("a",0)) + int(a.get('b',0))})
    return r
def index(request):

    return HttpResponse("<h1>Index</h1><h3>Index page</h3>")

def about(request):

    return HttpResponse("<h1>About</h1>")  

def contact(request): 
    return HttpResponse("<h1>Contact</h1>")