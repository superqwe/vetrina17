from pprint import pprint as pp

from .models import Tipo, Creazione

def menu_collezioni():
    perline = Creazione.objects.all()

    anni_perline = sorted(set([creazione.anno for creazione in perline]), reverse=True)

    uncinetto = []
    return anni_perline, uncinetto

def collezione_anno(tipo, anno):
    if tipo:
        collezione = Creazione.objects.filter(anno=anno)

        return collezione