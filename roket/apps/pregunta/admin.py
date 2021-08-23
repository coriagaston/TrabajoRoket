from django.contrib import admin
from .models import Pregunta, Respuesta
# Register your models here.

class ElegirRespuestaInline(admin.TabularInline):
	model = Respuesta

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (ElegirRespuestaInline, )
	list_display = ['la_pregunta']
	search_fields = ['texto', 'respuestas__texto']


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)


