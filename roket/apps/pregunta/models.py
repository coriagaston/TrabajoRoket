from django.db import models

from apps.core.models import TimeModel
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User



import random


class Estadisticas(models.Model):
	pass



class Categoria(models.Model):
	nombre = models.CharField(max_length = 30)

	
	def __str__(self):
		return self.nombre



class Pregunta(TimeModel):
	numero_de_respuesta = 1
	la_pregunta = models.TextField(verbose_name='Texto de la pregunta' )
	max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje',default=3,decimal_places=2,max_digits=6)
	Categoria = models.ForeignKey(Categoria, related_name = 'la_categoria', on_delete=models.CASCADE)

	def __str__(self):
		return self.la_pregunta

class Respuesta(models.Model):

	maximo_respuesta = 3

	respuesta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Esta seguro de esta respueta?',default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')
	


	def __str__(self):
		return self.texto

class Perfil_Usuario(models.Model):
	perfil_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total',default=0,decimal_places=2, max_digits=10)

	def crear_intentos(self, pregunta):
		intento = PreguntasRespondidas(pregunta=pregunta,Perfil_User=self)
		intento.save()

	def obtener_nuevas_preguntas(self):
		respondidas = PreguntasRespondidas.objects.filter(Perfil_User=self).values_list('pregunta__pk', flat=True)
		preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
		if not preguntas_restantes.exists():
			return None
		return random.choice(preguntas_restantes)

	def validar_intento(self,pregunta_respondida, respuesta_selecionada):
		if pregunta_respondida.respuesta_id != respuesta_selecionada.respuesta_id:
			return 

		pregunta_respondida.respuesta_selecionada = respuesta_selecionada
		if respuesta_selecionada.correcta is True:
			pregunta_respondida.correcta = True
			pregunta_respondida.puntaje = respuesta_selecionada.pregunta.max_puntaje
			pregunta_respondida.respuesta = respuesta_selecionada

		pregunta_respondida.save()


class PreguntasRespondidas(models.Model):
	Perfil_User = models.ForeignKey(Perfil_Usuario, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, null=True)
	correcta = models.BooleanField(verbose_name='¿Es tu respuesta correcta?', default=False, null=False)
	puntaje = models.DecimalField(verbose_name='Su puntaje',default=0, decimal_places=2, max_digits=6)


 
