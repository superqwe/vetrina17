from django.contrib import admin
from .models import Creazione, Evento, Messaggio, Tipo


# Register your models here.

class CreazioneOption(admin.ModelAdmin):
    list_display = ('anno', 'tipo', 'nome', 'descrizione', 'foto')
    list_display_links = ('nome',)
    list_filter = ('tipo', 'anno')
    ordering = ('-anno', 'tipo', 'nome')


admin.site.register(Creazione, CreazioneOption)
admin.site.register(Evento)
admin.site.register(Messaggio)
admin.site.register(Tipo)
