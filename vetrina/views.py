from django.shortcuts import render_to_response
from django.http import HttpResponse
from pprint import pprint as pp

import vetrina.services as services

LARA =  'Lara BjYou'

def home(request):
    lara = LARA
    nav_attivo = 'home'

    return render_to_response('vetrina/home.html', locals(), )

def collezioni(request, tipo=None, anno=None):
    lara = LARA
    nav_attivo = 'collezioni'
    menu_perline, menu_uncinetto = services.menu_collezioni()
    collezione_anno = services.collezione_anno(tipo, anno)

    return render_to_response('vetrina/collezioni.html', locals())


def eventi(request):
    lara = LARA
    nav_attivo = 'eventi'
    lista_eventi = services.lista_eventi()

    return render_to_response('vetrina/eventi.html', locals(), )

def contatti(request):
    lara = LARA
    nav_attivo = 'contatti'

    return render_to_response('vetrina/contatti.html', locals(), )

def about(request):
    lara = LARA
    nav_attivo = 'about'

    return render_to_response('vetrina/about.html', locals(), )

