from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from pprint import pprint as pp

import vetrina.services as services
from vetrina.forms import MessaggioForm

LARA = 'Lara BjYou'


def home(request):
    lara = LARA
    nav_attivo = 'home'

    return render_to_response('vetrina/home.html', locals(), )


def collezioni(request, tipo=None, anno=None):
    #todo: zoom su click immagine
    lara = LARA
    nav_attivo = 'collezioni'
    menu_perline, menu_uncinetto = services.menu_collezioni()
    collezione_anno = services.collezione_anno(tipo, anno)

    return render_to_response('vetrina/collezioni.html', locals())


def eventi(request):
    #todo: ordinare per data
    #todo: link nuova finestra
    lara = LARA
    nav_attivo = 'eventi'
    lista_eventi = services.lista_eventi()

    return render_to_response('vetrina/eventi.html', locals(), )


def contatti(request):
    lara = LARA
    nav_attivo = 'contatti'
    messaggio_inviato = False

    if request.method == 'POST':
        form_messaggio = MessaggioForm(request.POST)

        if form_messaggio.is_valid():
            messaggio = form_messaggio.save(commit=False)
            messaggio.nome = request.POST['nome']
            messaggio.email = request.POST['email']
            messaggio.messaggio = request.POST['messaggio']
            messaggio.save()

            messaggio_inviato = True

    else:
        form_messaggio = MessaggioForm()

    return render(request, 'vetrina/contatti.html',
                  {'form_messaggio': form_messaggio, 'nav_attivo': nav_attivo, 'lara': lara,
                   'messaggio_inviato': messaggio_inviato})


def about(request):
    lara = LARA
    nav_attivo = 'about'

    return render_to_response('vetrina/about.html', locals(), )
