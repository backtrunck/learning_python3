"""ecomstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import  url, include
from django.urls import path, re_path
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')),
    #re_path(r'',include('catalog.urls')),
    re_path('static/(?P<path>.*$)',serve,
    {'document_root':'/home/lcreina/Documentos/programacao/python3/django.projects/ecomstore/ecomstore/static',}),
]
#urlpatterns += path('catalog/','preview.views.home',name='home')
#urlpatterns += path('catalog/',include('preview.urls'))
#urlpatterns += patterns('',
    #other commented code here
#    (r'^catalog/$','preview.views.home'),)
