from django.shortcuts import render_to_response
from django.http import HttpResponse
from pprint import pprint as pp

import vetrina.services as services

LARA =  'Lara BjYou'

def home(request):
    lara = LARA
    return render_to_response('vetrina/home.html', locals(), )

def collezioni(request):
    lara = LARA
    menu_perline, menu_uncinetto = services.menu_collezioni()
    return render_to_response('vetrina/collezioni.html', locals(), )

def eventi(request):
    lara = LARA
    return render_to_response('vetrina/eventi.html', locals(), )

def contatti(request):
    lara = LARA
    return render_to_response('vetrina/contatti.html', locals(), )

def about(request):
    lara = LARA
    return render_to_response('vetrina/about.html', locals(), )

