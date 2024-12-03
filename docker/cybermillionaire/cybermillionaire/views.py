#views.py file


from django.shortcuts import HttpResponse
from django import template
#from export import export_questions as export
#mport cybermillionaire/cybermillionaire/export.py as e
#from cybermillionaire.export import export_questions as e
import cybermillionaire.export as e


def index(request):
    t = template.loader.get_template('index.html')
    html = t.render()
    return HttpResponse(html)
    
def start1(request):        #K-8 Level
    e.export_questions('1')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def start2(request):        #High School Level
    e.export_questions('2')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

    
def start3(request):        #College Level
    e.export_questions('3')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)
    
    
def start4(request):        #College + Technical Level
    e.export_questions('4')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

# Dynamic views
def dynamic_start1(request):  # Dynamic K-8 Level
    e.export_questions('dynamic-1')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start2(request):  # Dynamic High School Level
    e.export_questions('dynamic-2')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start3(request):  # Dynamic College Level
    e.export_questions('dynamic-3')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start4(request):  # Dynamic College + Technical Level
    e.export_questions('dynamic-4')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)
