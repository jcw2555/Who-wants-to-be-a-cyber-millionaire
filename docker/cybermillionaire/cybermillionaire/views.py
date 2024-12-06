#views.py file


from django.shortcuts import HttpResponse
from django import template
import cybermillionaire.export as e


def index(request):
    t = template.loader.get_template('index.html')
    html = t.render()
    return HttpResponse(html)
    
def start1(request):        # Static Primary School Level
    e.export_questions('1')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def start2(request):        # Static Secondary School Level
    e.export_questions('2')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

    
def start3(request):        # Static College Level
    e.export_questions('3')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)
    
    
def start4(request):        # Static Expert Level
    e.export_questions('4')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

# Dynamic views
def dynamic_start1(request):  # Dynamic Primary School Level
    e.export_questions('dynamic-1')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start2(request):  # Dynamic Secondary School Level
    e.export_questions('dynamic-2')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start3(request):  # Dynamic College Level
    e.export_questions('dynamic-3')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)

def dynamic_start4(request):  # Dynamic Expert Level
    e.export_questions('dynamic-4')
    t = template.loader.get_template('game.html')
    html = t.render()
    return HttpResponse(html)
