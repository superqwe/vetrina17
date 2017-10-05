from django.contrib import admin
from .models import Creazione, Evento, Messaggio, Tipo


# Register your models here.

class CreazioneOption(admin.ModelAdmin):
    list_display = ('anno', 'tipo', 'nome', 'descrizione', 'foto')
    list_display_links = ('nome',)
    list_filter = ('tipo', 'anno')
    ordering = ('-anno', 'tipo', 'nome')


class EventoOption(admin.ModelAdmin):
    date_hierarchy = 'dal'
    list_display = ('nome', 'luogo', 'dal', 'al', 'link', 'descrizione')
    list_display_links = ('nome',)
    ordering = ('-dal', 'luogo')


class MessaggioOption(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_display = ('nome', 'data', 'email', 'messaggio')
    list_display_links = ('nome',)
    ordering = ('-data',)


class TipoOption(admin.ModelAdmin):
    ordering = ('tipo',)


admin.site.register(Creazione, CreazioneOption)
admin.site.register(Evento, EventoOption)
admin.site.register(Messaggio, MessaggioOption)
admin.site.register(Tipo, TipoOption)
