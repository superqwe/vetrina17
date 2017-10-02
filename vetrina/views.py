from django.shortcuts import render_to_response
from django.http import HttpResponse
from pprint import pprint as pp

LARA =  'Lara BjYou'

def home(request):
    lara = LARA
    return render_to_response('vetrina/home.html', locals(), )

def collezioni(request):
    lara = LARA
    return render_to_response('vetrina/home.html', locals(), )

def eventi(request):
    lara = LARA
    return render_to_response('vetrina/home.html', locals(), )

def contatti(request):
    lara = LARA
    return render_to_response('vetrina/home.html', locals(), )

def about(request):
    lara = LARA
    return render_to_response('vetrina/home.html', locals(), )

