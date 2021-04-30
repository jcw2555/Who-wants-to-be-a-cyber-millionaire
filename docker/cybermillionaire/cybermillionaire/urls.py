"""cybermillionaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import reverse
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^k-8', views.start1, name='k8'),  #K-8th
    url(r'^high-school', views.start2, name='hs'),  #HS
    url(r'^college', views.start3, name='college'),  #college
    url(r'^college-tech', views.start4, name='tech'),  #college+ tech
    url(r'', views.index, name='start-page'),
    
    ]

    
    
