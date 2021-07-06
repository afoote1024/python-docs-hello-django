from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<p>Hello, Azure!  Python Django</p>
                        <p>- GitHub python-docs-hello-django/hello/views.py</p>"
                       
                       )
