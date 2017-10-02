from django.shortcuts import render_to_response
from django.http import HttpResponse
from pprint import pprint as pp

def index(request):
    lara = 'Lara BjYou'
    return render_to_response('vetrina/index.html', locals(), )
