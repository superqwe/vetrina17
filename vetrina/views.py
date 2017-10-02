from django.shortcuts import render_to_response
from django.http import HttpResponse
from pprint import pprint as pp

def index(request):
    return render_to_response('vetrina/index.html', locals(), )
