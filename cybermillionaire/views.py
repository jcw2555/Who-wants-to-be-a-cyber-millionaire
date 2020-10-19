#views.py file


from django.shortcuts import HttpResponse
from django import template
from export import export_questions as export

def index(request):
    t = template.loader.get_template('index.html')
    html = t.render()
    return HttpResponse(html)
    
def start1(request):        #K-8 Level
    t = template.loader.get_template('start.html')
    html = t.render()
    export('1')
    return HttpResponse(html)

def start2(request):        #High School Level
    t = template.loader.get_template('start.html')
    html = t.render()
    export('2')
    return HttpResponse(html)

def start3(request):        #College Level
    t = template.loader.get_template('start.html')
    html = t.render()
    export('3')
    return HttpResponse(html)
    
    
def start4(request):        #College + Technical Level
    t = template.loader.get_template('start.html')
    html = t.render()
    export('4')
    return HttpResponse(html)




