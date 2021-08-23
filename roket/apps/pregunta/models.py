from django.db import models

from apps.core.models import TimeModel
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User



class Pregunta(TimeModel):
	numero_de_respuesta = 1
	la_pregunta = models.TextField(verbose_name='Texto de la pregunta' )
	
	def __str__(self):
		return self.la_pregunta

class Respuesta(models.Model):

	maximo_respuesta = 3

	respuesta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Esta seguro de esta respueta?',default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')


	def __str__(self):
		return self.texto

class Perfil_Usuario(models.Model):
	perfil_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total',default=0,decimal_places=2, max_digits=10)



class PreguntasRespondidas(models.Model):
	perfil_usuario = models.ForeignKey(Perfil_Usuario, on_delete=models.CASCADE)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, related_name='intentos')
	correcta = models.BooleanField(verbose_name='¿Es tu respuesta correcta?', default=False, null=False)
	puntaje = models.DecimalField(verbose_name='Su puntaje',default=0, decimal_places=2, max_digits=6)


 
