from django.contrib import admin

from .models import Estilo, Obra, TipoDeObra, TrabajoRepresentado

# Register your models here.

admin.site.register(Obra)
admin.site.register(TrabajoRepresentado)
admin.site.register(TipoDeObra)
admin.site.register(Estilo)
