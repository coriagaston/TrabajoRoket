from django.db import models

from apps.core.models import TimeModel
# Create your models here.


class Pregunta(TimeModel):
	la_pregunta = models.TextField(verbose_name='Texto de la pregunta' )
	
	def __str__(self):
		return self.la_pregunta

class Respuesta(models.Model):

	respuesta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Esta seguro de esta respueta?',default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')


	def __str__(self):
		return self.texto