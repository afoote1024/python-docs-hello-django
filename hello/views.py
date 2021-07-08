from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, Azure!  
                        Python Django - GitHub python-docs-hello-django/hello/views.py")                            
