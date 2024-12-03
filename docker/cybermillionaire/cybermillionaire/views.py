#views.py file


from django.shortcuts import HttpResponse
from django import template
from export import export_questions as export




def index(request):
    t = template.loader.get_template('index.html')
    html = t.render()
    return HttpResponse(html)
    
def start1(request):        #K-8 Level
    export('1')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def start2(request):        #High School Level
    export('2')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

    
def start3(request):        #College Level
    export('3')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)
    
    
def start4(request):        #College + Technical Level
    export('4')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

# Dynamic views
def dynamic_start1(request):  # Dynamic K-8 Level
    export('dynamic-1')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start2(request):  # Dynamic High School Level
    export('dynamic-2')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start3(request):  # Dynamic College Level
    export('dynamic-3')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start4(request):  # Dynamic College + Technical Level
    export('dynamic-4')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)
