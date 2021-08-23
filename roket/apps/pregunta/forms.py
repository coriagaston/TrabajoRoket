from django import forms

from .models import Pregunta, Respuesta, PreguntasRespondidas


class ElegirInlineFormset(forms.BaseInlineFormSet):
 	def clean(self):
 		super(ElegirInlineFormset, self).clean()

 		respuesta_correcta = 1
 		for formulario in self.forms:
 			if not formulario.is_valid():
 				return 

 			if formulario.cleaned_data and formulario.cleaned_data.get('Correcta') is True:
 				respuesta_correcta += 1

 		try:
 			assert respuesta_correcta == Pregunta.numero_de_respuesta
 		except AssertionError:
 			raise forms.ValidationError('Solo una respuesta es permitida')