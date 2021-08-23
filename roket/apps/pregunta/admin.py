from django.contrib import admin
from .models import Pregunta, Respuesta, PreguntasRespondidas
from django.conf import settings



# Register your models here.

class ElegirRespuestaInline(admin.TabularInline):
	model = Respuesta
	can_delete = False
	max_num = Respuesta.maximo_respuesta


class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (ElegirRespuestaInline, )
	list_display = ['la_pregunta']
	search_fields = ['texto', 'respuestas__texto']



class PreguntasRespondidasAdmin(admin.ModelAdmin):
	list_display = ['pregunta', 'respuesta','correcta','puntaje']

	class meta:
		model = PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)


