from django.contrib import admin
from .models import Creazione, Evento, Messaggio, Tipo

# Register your models here.

admin.site.register(Creazione)
admin.site.register(Evento)
admin.site.register(Messaggio)
admin.site.register(Tipo)
