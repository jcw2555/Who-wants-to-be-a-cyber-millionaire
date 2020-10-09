#views.py file

from django.shortcuts import HttpResponse
from django import template

def index(request):
    t = template.loader.get_template('index.html')
    html = t.render()
    return HttpResponse(html)
    
def start(request):
    t = template.loader.get_template('start.html')
    html = t.render()
    return HttpResponse(html)

    
    
    




